# N-Gram Language Models with Good-Turing Smoothing

This project implements **unigram, bigram, trigram, and quadrigram language models** with **Good-Turing smoothing**. It computes sentence probabilities, log probabilities, and perplexity for validation and test sets, and saves detailed results to text files.

---

## Folder Structure

```
NGramModels/
├── train.txt                     # Training corpus (one sentence per line)
├── val.txt                       # Validation corpus
├── test.txt                      # Test corpus
├── Assignment_5_NLP_Good_Turing_Smoothing.ipynb # Jupyter Notebook
├── ngram_results/                # Output folder (auto-created)
│   ├── unigram_validation_results.txt
│   ├── unigram_test_results.txt
│   ├── bigram_validation_results.txt
│   ├── bigram_test_results.txt
│   ├── trigram_validation_results.txt
│   ├── trigram_test_results.txt
│   ├── quadrigram_validation_results.txt
│   ├── quadrigram_test_results.txt
│   └── summary_comparison.txt
```

---

## Input Format

- Each file (`train.txt`, `val.txt`, `test.txt`) must contain **one sentence per line**.  
- Sentences are tokenized by whitespace.  
- Example:

```
దీంతో ఇటు హాంకాంగ్ పోలీసులు , అటు ఆందోళనకారులకు మధ్య తీవ్రమైన ఘర్షణలు చోటు చేసుకుంటున్నాయి
మీ నాన్న ఇక రాడమ్మా
```

---

## On running, this will:

- Train unigram, bigram, trigram, and quadrigram models on the training corpus  
- Evaluate each model on validation and test sets  
- Save detailed results (sentence probabilities, n‑gram breakdowns, perplexity) into `ngram_results/`  
- Generate a summary comparison of perplexities across models  

---

## Methodology

1. **Training**  
   - Counts n‑grams and contexts from the training corpus  
   - Computes vocabulary size, unique n‑grams, and singletons (N1)  
   - Applies Good‑Turing smoothing for unseen n‑grams  

2. **Probability Estimation**  
   - For seen n‑grams: relative frequency with context counts  
   - For unseen n‑grams: smoothed probability via Good‑Turing  

3. **Sentence Evaluation**  
   - Computes log probability and probability of each sentence  
   - Provides detailed n‑gram breakdowns  

4. **Perplexity**  
   - Evaluates model performance on validation and test corpora  
   - Lower perplexity indicates better predictive performance  

5. **Summary Comparison**  
   - Saves a table of validation/test perplexities for all models  

