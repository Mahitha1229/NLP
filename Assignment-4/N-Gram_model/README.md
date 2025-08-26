# Telugu N-Gram Language Models

This repository builds unigram, bigram, trigram, and quadrigram models from a tokenized Telugu corpus. It is designed for corpus analysis, sentence probability evaluation, and reproducible research in Indian language NLP.

---

## Overview

This script processes a tokenized Telugu corpus and generates frequency-based n-gram models (n = 1 to 4). Each model is saved as a `.txt` file with tab-separated n-gram counts for downstream use in smoothing, sentence generation, or statistical analysis.

---

## Input

- `tokenized_telugu.txt`: A plain-text file where each line is a tokenized Telugu sentence (tokens separated by spaces).  
  Example:
  `<s> ప్రధాని నేడు సమావేశం నిర్వహించారు </s> <s> వర్షం కారణంగా రవాణా నిలిపివేశారు </s>`

  
---

## How It Works

1. **Load Corpus**  
 Reads and tokenizes each line from `tokenized_telugu.txt`.

2. **Build Models**  
 - **Unigram**: Single-token frequencies  
 - **Bigram**: Consecutive token pairs  
 - **Trigram**: Three-token sequences  
 - **Quadrigram**: Four-token sequences

3. **Save Outputs**  
 Each model is saved as a `.txt` file


---

## Usage

Save the file as `Assignment_4_NLP_N-gram_model.ipynb` and run it on Visual Studio Code. Make sure to have `Assignment_4_NLP_N-gram_model.ipynb` and `tokenized_telugu.txt` in the same folder

---

## Output Files
- `unigram_model.txt`
- `bigram_model.txt`
- `trigram_model.txt`
- `quadrigram_model.txt`
  

