# Bigram PMI Computation

This repository contains a Python script to compute **Pointwise Mutual Information (PMI)** scores for bigrams using unigram and bigram language models. It processes validation and test corpora, calculates PMI values, and outputs ranked bigram scores.

---

## What Is PMI?

PMI measures how much more often two words appear together than would be expected if they were independent:
A higher PMI indicates stronger association between the words.

---

## Folder Structure

```
PMI/
├── inputs/
│   ├── unigram_model.txt
│   ├── bigram_model.txt
│   ├── val.txt
│   └── test.txt
├── outputs/
│   ├── pmi_val.txt
│   └── pmi_test.txt
├── pmi.py
```

---

## How to Run

Make sure your input files are placed in the `inputs/` folder.

Then run:

```bash
python pmi.py

