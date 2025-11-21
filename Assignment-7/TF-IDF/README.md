# TF-IDF Vectorization Pipeline

This project implements a **TF-IDF (Term Frequency–Inverse Document Frequency)** pipeline for text datasets. It converts raw tokenized sentences into sparse numerical representations that can be used for machine learning models, clustering, or similarity analysis.

---

## What is TF-IDF?

TF-IDF is a statistical measure used to evaluate how important a word is to a document in a collection:

- **TF (Term Frequency):** How often a word appears in a document.
- **IDF (Inverse Document Frequency):** How rare the word is across all documents.
- **TF-IDF:** Combines both, giving higher weight to words that are frequent in a document but rare across the corpus.

This representation is widely used in **NLP tasks** such as document classification, information retrieval, and keyword extraction.

---

## Folder Structure

```
TF-IDF/
├── inputs/
│   ├── train.txt         # Training sentences (space-tokenized)
│   ├── val.txt           # Validation sentences
│   └── test.txt          # Test sentences
├── outputs/
│   └── tfidf_output/
│       ├── tfidf_train.npz
│       ├── tfidf_val.npz
│       ├── tfidf_test.npz
│       └── vocab.json
├── tfidf.py   # Main script
```




---

## How to Run

1. Place your tokenized text files (`train.txt`, `val.txt`, `test.txt`) inside the `inputs/` folder.  
   - Each line = one sentence  
   - Tokens separated by spaces  

2. Run the script:

```bash
python tfidf.py
