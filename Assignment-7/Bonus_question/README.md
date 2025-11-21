# Nearest Neighbor Search (Validation/Test → Train) using TF-IDF + Cosine Similarity

This project finds the nearest neighbor sentence in the training set for each sentence in the validation and test sets. It uses cosine similarity over precomputed TF-IDF vectors and supports batching for memory efficiency.

---

## Folder Structure

```
Bonus_question/
├── inputs/
│   ├── train.txt             # Training sentences (one per line, space-tokenized)
│   ├── val.txt               # Validation sentences
│   ├── test.txt              # Test sentences
│   ├── tfidf_train.npz       # Sparse TF-IDF matrix for train.txt
│   ├── tfidf_val.npz         # Sparse TF-IDF matrix for val.txt
│   └── tfidf_test.npz        # Sparse TF-IDF matrix for test.txt
├── outputs/
│   ├── nearest_neighbors_val_in_train.txt   # Nearest neighbors for val sentences in train
│   └── nearest_neighbors_test_in_train.txt  # Nearest neighbors for test sentences in train
├── code.py   # Main script
```

---

## How to Run

1. Place your tokenized sentence files and TF-IDF matrices inside the `inputs/` folder.  
   - Each line = one sentence  
   - Tokens separated by spaces  

2. Run the script:

```bash
python code.py
```

3. Outputs will be saved in the `outputs/` folder.

---

## Output Format

Each line in the output files has the format:

```
query_index<TAB>train_index<TAB>similarity<TAB>query_sentence<TAB>|||<TAB>train_sentence
```

Example:

```
1	284	0.2114	ఇక కోటాలో మెడికల్ , ఇంజినీరింగ్ కోచింగ్ సెంటర్లు చాలా ఉన్నాయి	|||	చాలా ఇబ్బందుల్లో ఉన్న
```

---

## Methodology

- Loads sentences from `.txt` files.  
- Loads sparse TF-IDF matrices from `.npz` files.  
- Computes cosine similarity between each query (val/test) and all training sentences.  
- Uses batching (`BATCH_SIZE = 500`) to avoid memory overload.  
- Finds the most similar training sentence for each query.  
- Estimates the number of operations (`≈ N_queries * N_train * D`) for reporting.  

---

## Notes

- Input sentences must be space-tokenized.  
- TF-IDF matrices must match the number of sentences in each file.  
- Self-similarity is excluded (queries are only compared against training set).  
- Batching ensures scalability for large datasets.  

---

## Requirements

- Python 3.x  
- numpy  
- scipy  
- scikit-learn  

Install with:

```bash
pip install numpy scipy scikit-learn
```

