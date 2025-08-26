# Telugu N-Gram Language Modeling with Smoothing Techniques

This repository implements a complete pipeline for building and evaluating n-gram language models (unigram to quadrigram) on a synthetic Telugu corpus. It includes automatic sentence generation, frequency-based modeling, and three smoothing techniques to compute sentence-level probabilities.

---

## Overview

The project performs the following tasks:

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

---

## Input Files

- `tokenized_telugu.txt`  
  A plain-text file where each line is a tokenized Telugu sentence. Tokens must be space-separated.  
  This is the only required input file — synthetic sentences are generated automatically.

---

## Output Files

- `generated_telugu_sentences.txt`  
  Contains 1000 automatically generated Telugu news-style sentences.

- `sentence_probabilities.tsv`  
  Tab-separated file with log-probabilities for each sentence under each model and smoothing method.

Example:

| Sentence ID | Model | Smoothing | LogProbability |
|----------|----------|----------|-----------------|
| 1	| 1-gram	| add_one	| -52.3607   |
|953	| 2-gram	| add_k	| -72.7905 |
| 88	| 3-gram	| token_type	| -60.9921 |
| 700 |	4-gram	| token_type	| -50.3087 |


