# Telugu Tokenization Pipeline using IndicCorpV2

This project provides a Unicode-aware tokenization pipeline for Telugu text using the [AI4Bharat IndicCorpV2](https://huggingface.co/datasets/ai4bharat/IndicCorpV2) dataset. It includes sentence and word tokenization, corpus statistics, and interactive input support.

---

## Dataset

- **Source**: [IndicCorpV2](https://huggingface.co/datasets/ai4bharat/IndicCorpV2)
- **Split Used**: `tel_Telu` (Telugu)
- **Access Method**: Streaming via  `datasets` library

---

##  Features

- Sentence segmentation using Telugu and Latin punctuation
- Word tokenization with Unicode-aware regex
- Handles dates, URLs, emails, numbers, and Telugu script
- Saves tokenized output to a `.txt` file
- Computes corpus statistics: sentence/word counts, TTR, averages
- Interactive tokenization for user input

---

## Installation 
```bash
pip install datasets
