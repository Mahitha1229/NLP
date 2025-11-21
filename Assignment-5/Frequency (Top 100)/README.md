# Good-Turing Frequency Table Generator

This project generates **Good-Turing frequency tables** for unigram, bigram, trigram, and quadrigram models. It estimates the probability mass of n-grams based on their counts and provides adjusted counts (`C*`) for smoothing unseen events.

---

## Folder Structure

```
GoodTuringTables/
├── tokenized_telugu.txt          # Full corpus (one sentence per line)
├── unigram_model.txt             # Precomputed unigram counts (ngram<TAB>count)
├── bigram_model.txt              # Precomputed bigram counts
├── trigram_model.txt             # Precomputed trigram counts
├── quadrigram_model.txt          # Precomputed quadrigram counts
├── Assignment_5_NLP_Frequency(Top-100).ipynb # Jupyter Notebook
├── unigram_frequency_table.txt   # Output frequency table for unigrams
├── bigram_frequency_table.txt    # Output frequency table for bigrams
├── trigram_frequency_table.txt   # Output frequency table for trigrams
├── quadrigram_frequency_table.txt# Output frequency table for quadrigrams
```

---

## Input Format

- **Corpus file** (`tokenized_telugu.txt`): one sentence per line, space-tokenized.  
- **Model files** (`*_model.txt`): each line contains `ngram<TAB>count`.  

Example (`bigram_model.txt`):

```
this is    120
is a       95
a sample   42
```

---

## On running this will:

- Compute vocabulary size from the corpus  
- Load n-gram counts from each model file  
- Generate Good-Turing frequency tables for unigram, bigram, trigram, and quadrigram models  
- Save results into `*_frequency_table.txt` files  

---

## Methodology

1. **Vocabulary Size**  
   - Counts unique tokens in the full corpus.

2. **Load N-Gram Counts**  
   - Reads model files containing n-gram counts.

3. **Good-Turing Smoothing**  
   - For each count `c`, computes:  
     - `Nc`: number of n-grams with count `c`  
     - `Nc+1`: number of n-grams with count `c+1`  
     - `C*`: adjusted count = `(c+1) * Nc+1 / Nc`  
     - Probability mass for count `c`: `Nc / N_total`

4. **Output Table**  
   - Saves results in tab-separated format with columns:  
     - `C (MLE)` — original count  
     - `Nc (GT Prob)` — probability mass for count `c`  
     - `C*` — adjusted count  

---

## Output Example

```
C (MLE)    Nc (GT Prob)    C*
1          0.00234567      1.2345
2          0.00123456      2.1111
3          0.00098765      3.0000
```

---


## Notes

- Only the first 100 distinct counts are included in the output table.  
- Adjust file paths in the script if your dataset is stored elsewhere.  
- The tables provide insight into how probability mass is redistributed for rare and unseen n-grams.  

