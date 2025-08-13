# Trie-Based Stemming Analysis

## Objective
This project explores morphological analysis using **prefix** and **suffix tries** to identify stems and suffixes in English nouns. The goal is to evaluate which trie structure provides more effective stemming based on branching heuristics.

---

## Dataset
- **File**: `brown_nouns.txt`
- **Source**: Extracted from the Brown Corpus
- **Content**: A list of English nouns, one per line

---

## Methodology

1. **Trie Construction**:
   - **Prefix Trie**: Inserts words from start to end.
   - **Suffix Trie**: Inserts reversed words to capture suffix patterns.

2. **Branching Heuristic**:
   - The node with **maximum branching** is considered the stem/suffix boundary.
   - Words are split into `stem + suffix` accordingly.

3. **Comparison**:
   - Total suffix lengths are calculated for both tries.
   - The trie with shorter cumulative suffix length is considered more effective.

---

## How to Run

Ensure `brown_nouns.txt` is in the same directory as the script.

```bash
python stem_trie.py
```
This will generate a text file as stemming_output.txt which contains stem+suffix pairs and a comparison summary.

---

## Output Format
Prefix Trie Stemming:
investigation = in+vestigation
primary = p+rimary

Suffix Trie Stemming:
investigation = on+investigati
primary = y+primar

Comparison:
Total suffix length in Prefix Trie: 123
Total suffix length in Suffix Trie: 98
Better stemming achieved by: Suffix Trie

---

## Interpretation
- Prefix Trie often splits early, resulting in short stems that may lack linguistic relevance.
- Suffix Trie captures common English suffixes (e.g., -ion, -y, -s) more effectively.
- Based on suffix length comparison, Suffix Trie provides better stemming performance for this dataset.

---
