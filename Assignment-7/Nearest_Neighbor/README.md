# Nearest Neighbor Finder using TF-IDF + Cosine Similarity

This project computes the **nearest neighbor sentence** for each input sentence using **cosine similarity** over precomputed **TF-IDF vectors**. It processes validation and test sets, identifies the most similar sentence for each, and outputs the results in a readable format.

---

## Folder Structure

```
Nearest_neighbor/
├── inputs/
│   ├── val.txt               # Validation sentences (one per line, space-tokenized)
│   ├── test.txt              # Test sentences
│   ├── tfidf_val.npz         # Sparse TF-IDF matrix for val.txt
│   └── tfidf_test.npz        # Sparse TF-IDF matrix for test.txt
├── outputs/
│   ├── nearest_neighbors_val.txt   # Nearest neighbors for validation set
│   └── nearest_neighbors_test.txt  # Nearest neighbors for test set
├── nearest_neighbor.py         # Main script
```

---

## How to Run

Make sure your TF-IDF matrices and sentence files are placed in the `inputs/` folder.

Then run:

```bash
python nearest_neighbor.py
```

This will generate:

- `nearest_neighbors_val.txt`
- `nearest_neighbors_test.txt`

Each line contains:

```
sentence_index<TAB>neighbor_index<TAB>similarity<TAB>sentence<TAB>|||<TAB>neighbor_sentence
```

---

##  Methodology

- Loads tokenized sentences from `.txt` files.
- Loads sparse TF-IDF matrices from `.npz` files.
- Computes **cosine similarity** between each sentence and all others.
- Finds the **most similar sentence** (excluding itself).
- Writes results with similarity scores and sentence pairs.

---

##  Output Format Example

```
1	48	0.6235	ఇక కోటాలో మెడికల్ , ఇంజినీరింగ్ కోచింగ్ సెంటర్లు చాలా ఉన్నాయి	|||	ఇక వంశీ కృష్ణ ఆకెళ్ళ దర్శకునిగా చాలా సేఫ్ వెళ్ళడానికి ప్రయత్నించాడు 
```

This means sentence 3’s nearest neighbor is sentence 17 with a cosine similarity of 0.8421.

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

---

##  Notes

- Input sentences must be **space-tokenized**.  
- TF-IDF matrices must match the number of sentences in each file.  
- Self-similarity is excluded during neighbor search.  

---


