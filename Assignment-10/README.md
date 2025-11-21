# Hidden Markov Model POS Tagger with K-Fold Evaluation

This project implements a **Hidden Markov Model (HMM)** for **Part-of-Speech (POS) tagging** using supervised training and **Viterbi decoding**. It supports **k-fold cross-validation** and evaluates performance using **precision, recall, and F1 score**.

---

## Folder Structure

```
├── wsj_pos_tagged_en.txt     # Tagged corpus (word/tag format)
├── pos.ipynb             # Jupyter Notebook
```

---

## Corpus Format

Each line in `wsj_pos_tagged_en.txt` contains a space-separated sentence with tokens in `word/tag` format:

```
The/DT quick/JJ brown/NN fox/NN jumps/VBZ ./.
```

---

## On running, this will:

- Load the tagged corpus
- Split it into `k=5` folds
- Train the HMM on 4 folds and test on 1 (repeated for each fold)
- Print per-fold macro F1 scores and the average across all folds

---

## Methodology

1. **Corpus Loading**  
   Parses each line into `(word, tag)` pairs, skipping malformed tokens.

2. **K-Fold Splitting**  
   Shuffles the dataset with a fixed seed and splits into `k` folds for cross-validation.

3. **HMM Training**  
   - Learns **emission probabilities**: P(word | tag)  
   - Learns **transition probabilities**: P(tag_i | tag_{i-1})  
   - Applies Laplace smoothing to handle unseen words and transitions.

4. **Viterbi Decoding**  
   Uses dynamic programming to find the most probable tag sequence for a sentence.

5. **Evaluation**  
   - Computes precision, recall, and F1 per tag  
   - Reports **macro-averaged F1** across all tags  
   - Macro F1 ensures balanced evaluation across frequent and rare tags.

---

## Output Example

```
=== Fold 1/5 ===
Macro F1 = 0.8762

=== Fold 2/5 ===
Macro F1 = 0.8821

...

Average Macro F1 Across Folds: 0.8794
```

---

## Why This Matters

- **POS tagging** is a foundational task in NLP, supporting parsing, information extraction, and downstream models.  
- **HMMs** provide a probabilistic framework that balances observed word-tag frequencies with sequence constraints.  
- **Cross-validation** ensures robust evaluation and avoids overfitting to a single train/test split.

---

---

## Notes

- The model uses `<s>` as the start symbol and `<UNK>` for unknown words.  
- Probabilities are computed in log-space for numerical stability.  
- Evaluation assumes gold and predicted tag sequences are aligned.
