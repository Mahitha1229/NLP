# Telugu Bigram Language Model with Smoothing Techniques

This repository implements a bigram-based language model for Telugu using a tokenized corpus. It applies three smoothing techniques : 
- Add-One
- Add-K
- Token-Type
to estimate conditional probabilities for bigrams and outputs the results in a structured format.

---

## Overview

The script reads a tokenized Telugu corpus, builds bigram frequency counts, and computes smoothed probabilities for each bigram using:

- **Add-One Smoothing**  
- **Add-K Smoothing** (with k = 0.3)  
- **Token-Type Smoothing** (heuristic weights)

The results are saved to a tab-separated file for inspection or downstream evaluation.

---

## Input

- `tokenized_telugu.txt`  
  A plain-text file where each line is a tokenized Telugu sentence. Tokens should be space-separated.  
  Example:
  `ప్రధాని నేడు సమావేశం నిర్వహించారు వర్షం కారణంగా రవాణా నిలిపివేశారు`

  
---

## How It Works

1. **Corpus Loading**  
 Reads and tokenizes each sentence from the input file.

2. **N-Gram Counting**  
 - Adds `<s>` and `</s>` tokens to mark sentence boundaries  
 - Computes unigram and bigram frequencies

3. **Smoothing Application**  
 For each bigram, computes:
 - Add-One smoothed probability  
 - Add-K smoothed probability  
 - Token-Type smoothed probability (using a fixed weight of 1.5 per token)

4. **Output Generation**  
 Saves all results to `smoothing_output.txt` with the following columns:
- Bigram
- Count
- PrefixCount
- AddOne
- AddK
- TokenType

---


---

## Usage

Save the file as `Assignment_4_NLP_Smoothing_Techniques.ipynb` and execute it on Visual Studio Code. Make sure to place `Assignment_4_NLP_Smoothing_Techniques.ipynb` and `tokenized_telugu.txt` in the same folder

---

## Output

Output is stored in `smoothing_output.txt` file

Example:

`('ప్రధాని', 'నేడు')	12	20	0.0152	0.0147	0.0139`  

`('వర్షం', 'కారణంగా')	8	15	0.0123	0.0119	0.0108`
