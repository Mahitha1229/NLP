# Byte Pair Encoding (BPE) & WordPiece Tokenization from Scratch
### Using `tokenized_telugu.txt` Corpus

This project implements **Byte Pair Encoding (BPE)** and **WordPiece** tokenization algorithms **from scratch**, without using any external NLP tokenization libraries like HuggingFace Tokenizers or SentencePiece.

The script processes a tokenized Telugu corpus and generates:
- Merge operations list
- Vocabulary files

---

## Project Structure

```
├── tokenized_telugu.txt # Input tokenized corpus (one sentence per line)
└── code.py # Implementation script

```


---

## How to Run the Script

### Make sure `tokenized_telugu.txt` is present
Format example:

```
అమెరికా అధ్యక్షుడు డొనాల్డ్ ట్రంప్ కు రాష్ట్రపతి భవన్ వద్ద ఘనస్వాగతం లభించింది

```

### Run the program
```bash
python code.py
 ```
### Output files generated

| Algorithm     | Setting                   | Output Files                                                   |
| ------------- | ------------------------- | -------------------------------------------------------------- |
| **BPE**       | 32000 merge steps         | `bpe_merges_32000.txt`, `bpe_vocab_32000.txt`                  |
| **BPE**       | Target vocab size = 32000 | `bpe_merges_vocab32000.txt`, `bpe_vocab_32000_by_size.txt`     |
| **WordPiece** | Target vocab size = 32000 | `wordpiece_merges_vocab32000.txt`, `wordpiece_vocab_32000.txt` |

### Implementation Summary

BPE Algorithm Flow:
- Load corpus and compute word frequencies
- Convert each word into characters + </w>
- Count frequency of adjacent symbol pairs
- Merge most frequent pair
- Update vocabulary each iteration
- Stop when merge step limit or vocab size limit reached

WordPiece Algorithm Flow:
- Initialize tokens as character set + </w>
- Calculate pair scores:

```
score = pair_freq / (token_freq[left] * token_freq[right])

```
- Merge highest scoring pair
- Update sequences + vocab
- Stop when vocab size hits 32000
