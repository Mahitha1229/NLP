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



