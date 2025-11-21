# TF-IDF Sentence Preprocessing and Computation

## Overview
This project demonstrates how to preprocess text data and compute **TF-IDF (Term Frequency–Inverse Document Frequency)** scores for each term in a set of sentences.  
The code includes:
- Preprocessing with special tokens for numbers, URLs, and punctuation.
- Functions to compute normalized term frequency (TF).
- Functions to compute inverse document frequency (IDF).
- Functions to compute TF-IDF scores using log scaling.
- Saving results to a text file (`tfidf_output.txt`).

---

## Preprocessing Rules
Each sentence is preprocessed as follows:
1. **Lowercasing** → All text is converted to lowercase.
2. **Numbers** → Any numeric value is replaced with the token `NUMBER`.
3. **URLs** → Any URL is replaced with the token `URL`.
4. **Punctuation** → Any punctuation symbol is replaced with the token `PUNCT`.
5. **Tokenization** → Sentences are split into tokens by whitespace.

Example:
```
Input: "Visit https://example.com for 123 apples!"
Output: ['visit', 'URL', 'for', 'NUMBER', 'apples', 'PUNCT']

```


---

## Project Structure
- `code.py` → Main implementation (preprocessing, TF, IDF, TF-IDF).
- `tfidf_output.txt` → Output file containing preprocessed sentences and TF-IDF scores.

---

## Requirements
- Python 3.7+
- No external libraries required (uses only built-in modules: `re`, `math`, `collections`).

---

## How to Run
1. Save the code in a file named `code.py`.
2. Run the script:
```
python code.py

```
