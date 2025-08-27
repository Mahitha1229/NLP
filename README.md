# NLP Assignments Repository

This repository contains all my **Natural Language Processing (NLP)** lab assignments, organized by topics and modules. It includes Python code, Jupyter notebooks, datasets, and outputs for various NLP concepts and algorithms.
---

## Assignments Overview

### **Assignment 1 – Tokenizer**
This project provides a Unicode-aware tokenization pipeline for Telugu text using the AI4Bharat IndicCorpV2 dataset.

The features are : 

- Sentence segmentation using Telugu and Latin punctuation
- Word tokenization with Unicode-aware regex
- Handles dates, URLs, emails, numbers, and Telugu script
- Saves tokenized output to a .txt file
- Computes corpus statistics: sentence/word counts, TTR, averages
---
### **Assignment 2 :**

**1. DFA**

The objective is to design and implement a Deterministic Finite Automaton (DFA) that recognizes simplified English words according to the following rules:

- The word must start with a lowercase English letter (a–z).
- The rest of the word may contain only lowercase English letters (a–z).
- Any uppercase letters, digits, spaces, or special characters make the word invalid.

**2. FST**

This project simulates a Finite State Transducer (FST) that processes nouns from the Brown corpus and generates their morphological features in both singular and plural forms.

The objective is to : 

- Read nouns from `brown_nouns.txt`
- Apply pluralization rules using FST logic
- Output morphological tags in the format:  
  `root+N+SG` for singular  
  `root+N+PL` for plural
- Reject invalid pluralizations with `"Invalid Word"`

---

## **Assignment 3:**

**1. Trie-Based Stemming Analysis**

This project explores morphological analysis using **prefix** and **suffix tries** to identify stems and suffixes in English nouns. The goal is to evaluate which trie structure provides more effective stemming based on branching heuristics.

The interpretation is :

- Prefix Trie often splits early, resulting in short stems that may lack linguistic relevance.
- Suffix Trie captures common English suffixes (e.g., -ion, -y, -s) more effectively.
- Based on suffix length comparison, Suffix Trie provides better stemming performance for this dataset.

**2. Telugu Token Frequency Analysis**

This project analyzes **Telugu text tokens** and visualizes the **Top 100 most frequent tokens** in a **horizontal bar chart**.  
It uses **Matplotlib** for visualization, **Counter** from Python's `collections` for frequency calculation, and a **custom Telugu font (.ttf)** to ensure proper rendering of Telugu characters.

---

## **Assignment 4:**

**1. N-gram Model**

This project builds unigram, bigram, trigram, and quadrigram models from a tokenized Telugu corpus. It is designed for corpus analysis, sentence probability evaluation, and reproducible research in Indian language NLP.

This script processes a tokenized Telugu corpus and generates frequency-based n-gram models (n = 1 to 4). Each model is saved as a `.txt` file with tab-separated n-gram counts for downstream use in smoothing, sentence generation, or statistical analysis.

It works by:
- *Loading Corpus* : Reads and tokenizes each line from `tokenized_telugu.txt`.
- *Building Models* :
- `Unigram`: Single-token frequencies
- `Bigram`: Consecutive token pairs
- `Trigram`: Three-token sequences
- `Quadrigram`: Four-token sequences
- Saving the output: Each model is saved as a `.txt` file

---

**2. Smoothing Techniques**

This repository implements a bigram-based language model for Telugu using a tokenized corpus. It applies three smoothing techniques :

- Add-One
- Add-K
- Token-Type to estimate conditional probabilities for bigrams and outputs the results in a structured format.

**Overview**

The script reads a tokenized Telugu corpus, builds bigram frequency counts, and computes smoothed probabilities for each bigram using:

- Add-One Smoothing
- Add-K Smoothing (with k = 0.3)
- Token-Type Smoothing (heuristic weights)
- The results are saved to a tab-separated file for inspection or downstream evaluation.

---

**3. Telugu N-Gram Language Modeling with Smoothing Techniques**

This project performs the following tasks: 

1. **Synthetic Sentence Generation**  
   Automatically generates 1000 Telugu news-style sentences using topic-specific vocabulary and realistic templates. No external input file is required.

2. **Corpus Loading and Preprocessing**  
   Loads a pre-tokenized Telugu corpus (`tokenized_telugu.txt`) and prepares evaluation sentences with `<s>` and `</s>` markers.

3. **N-Gram Model Construction**  
   Builds unigram, bigram, trigram, and quadrigram frequency models from the tokenized corpus.

4. **Smoothing Techniques**  
   Applies:
   - Add-One Smoothing  
   - Add-K Smoothing (k = 0.3)  
   - Token-Type Smoothing (heuristic weight = 1.5)

5. **Sentence Probability Evaluation**  
   Computes log-probabilities for each of the 1000 synthetic sentences under each model and smoothing technique.

6. **Output Saving**  
   Saves results to a tab-separated file for inspection or downstream analysis.
