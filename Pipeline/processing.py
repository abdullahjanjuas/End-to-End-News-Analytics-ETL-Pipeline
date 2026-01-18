from models import kw_model, embedding_model, sent_tokenizer, sent_model, SENTIMENT_LABELS
import torch
import torch.nn.functional as F

def prepare_text(title, content, max_words=300):
    title = "" if not isinstance(title, str) else title
    content = "" if not isinstance(content, str) else content
    body = " ".join(content.split()[:max_words])
    return f"{title}. {body}".strip()

def extract_keywords(text, top_k=7):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 1),
        stop_words="english",
        use_mmr=True,
        diversity=0.6,
        top_n=top_k
    )
    return [kw for kw, _ in keywords]

def embed_texts(texts, batch_size=64):
    return embedding_model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True
    )

def analyze_sentiment(text):
    inputs = sent_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    with torch.no_grad():
        outputs = sent_model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)[0]

    label = SENTIMENT_LABELS[int(torch.argmax(probs))]
    return label