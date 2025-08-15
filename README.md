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
- Interactive tokenization for user input

---

### **Assignment 2 - DFA**
The objective is to design and implement a Deterministic Finite Automaton (DFA) that recognizes simplified English words according to the following rules:

- The word must start with a lowercase English letter (a–z).
- The rest of the word may contain only lowercase English letters (a–z).
- Any uppercase letters, digits, spaces, or special characters make the word invalid.

This validator accepts non-empty strings composed exclusively of lowercase English letters (a–z). It includes:

- Interactive command-line validation
- Batch testing for datasets
- DFA visualization using networkx and matplotlib
- Educational insights into automata theory

