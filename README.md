# End-to-End News Analytics ETL Pipeline (Data Engineering & NLP)

## Overview
This project implements a **production-style end-to-end ETL pipeline** for large-scale news analytics.  
The system extracts unstructured news articles from Dawn’s website, transforms raw text into enriched semantic representations using NLP, and loads structured, analytics-ready datasets for downstream analysis and visualization.

The pipeline is designed with **data engineering principles**, treating NLP as a transformation layer rather than a standalone modeling task.

---

## Architecture Overview

**Extract → Transform → Load (ETL)**

1. **Extract**
   - Automated web ingestion of news articles using Selenium
   - Captures article text, metadata (date, title, URL), and location information

2. **Transform**
   - Text cleaning, normalization, and truncation
   - Keyword extraction using KeyBERT
   - Semantic embeddings using SentenceTransformers (MPNet)
   - Unsupervised clustering (HDBSCAN) for topic discovery
   - Semi-supervised category classification using Logistic Regression
   - Sentiment analysis using a transformer-based model (RoBERTa)

3. **Load**
   - Materialization of structured CSV data marts
   - Outputs optimized for BI tools and analytical workloads

---

## Project Structure

.
├── dawn_scraper.py # Data ingestion layer (web scraping)
├── clean.py # Text cleaning and preprocessing
├── models.py # NLP models (embeddings, keywords, sentiment)
├── processing.py # Reusable NLP transformation functions
├── process.ipynb # Pipeline orchestration and data generation
├── EDA.ipynb # Exploratory data analysis
└── output/
├── csv1_core.csv
├── csv2_embeddings.csv
├── csv3_keywords.csv
└── csv4_metadata.csv


---

## ETL Pipeline Details

### 1. Data Extraction
- Scrapes news articles using Selenium to handle dynamic content
- Ensures reproducible and scalable data collection
- Produces a raw dataset of unstructured text with metadata

### 2. Data Transformation
- **Text Preparation:** title + truncated body for consistent modeling
- **Keyword Extraction:** KeyBERT with MMR for diversity
- **Embeddings:** SentenceTransformers (`all-mpnet-base-v2`) with normalized vectors
- **Clustering:** HDBSCAN for density-based topic discovery
- **Category Assignment:** 
  - Manual mapping of high-confidence clusters
  - Logistic Regression trained on embeddings to generalize categories
- **Sentiment Analysis:** Transformer-based sentiment inference with controlled batch processing

### 3. Data Loading (Analytics-Ready Outputs)
The pipeline produces multiple structured datasets:

- **Core Dataset:**  
  `id, date, category, location, sentiment`
- **Embeddings Dataset:**  
  `id, embedding`
- **Keywords Dataset:**  
  `id, date, keyword`
- **Metadata Dataset:**  
  `id, title, url`

These outputs are designed for **BI dashboards, trend analysis, and downstream ML workloads**.

---

## Key Engineering Highlights
- Modular pipeline design with separation of concerns
- NLP treated as a transformation layer within ETL
- Semi-supervised learning to handle label scarcity
- Scalable inference with compute-aware constraints
- Analytics-first data modeling

---

## Downstream Usage
The outputs of this pipeline are consumed by a **Power BI dashboard** to analyze:
- Sentiment trends over time
- Category-wise and region-wise media sentiment
- Keyword-driven topic exploration

---

## Tech Stack
- **Programming:** Python
- **Data Engineering:** Selenium, Pandas
- **NLP & ML:** SentenceTransformers, KeyBERT, Hugging Face Transformers, HDBSCAN, Scikit-learn
- **Deep Learning:** PyTorch
- **Analytics:** Power BI (downstream)

---

## Use Cases
- Media sentiment analysis
- Regional and category-based news insights
- Content analytics pipelines
- NLP-powered decision support systems

---

## Disclaimer
This project is for **educational and analytical purposes only**.  
All data is sourced from publicly available news articles.
