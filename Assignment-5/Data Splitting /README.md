# Dataset Splitter for Telugu Corpus

This project provides a simple utility to **split a tokenized text dataset** into training, validation, and test sets. The script ensures reproducibility by shuffling with a fixed random seed.

---

## Folder Structure

```
├── tokenized_telugu.txt      # Input dataset (one sentence per line)
├── data_splits/              # Output folder (auto-created)
│   ├── train.txt             # Training set
│   ├── val.txt               # Validation set
│   └── test.txt              # Test set
├── Assignment_5_NLP_Data_Splitting.ipynb  # Jupyter Notebook 

```

---

## Input Format

- The input file (`tokenized_telugu.txt`) must contain **one sentence per line**.  
- Empty lines are ignored automatically.

Example:

```
ఇది ఒక వాక్యం .
ఇది రెండవ వాక్యం .
```

---

## On running, this will:

- Shuffle the dataset with a fixed seed (`42`) for reproducibility  
- Split into:
  - **Test set:** first 500 sentences  
  - **Validation set:** next 500 sentences  
  - **Training set:** remaining sentences  
- Save results into the `data_splits/` folder

---

## Methodology

1. **Load Sentences**  
   Reads all non-empty lines from the input file.

2. **Shuffle Data**  
   Uses `random.seed(42)` to ensure consistent splits across runs.

3. **Split Data**  
   - Test: first 500 sentences  
   - Validation: next 500 sentences  
   - Train: all remaining sentences  

4. **Save Outputs**  
   Writes each split into separate `.txt` files under `data_splits/`.

---

## Output Example

```
data_splits/
├── train.txt   # ~N-1000 sentences
├── val.txt     # 500 sentences
└── test.txt    # 500 sentences
```

---

## Notes

- Adjust split sizes by modifying the slicing in `split_data()` if needed.  
- The script automatically creates the `data_splits/` folder if it does not exist.  
- Shuffling ensures that train/val/test sets are representative of the whole dataset.

---
