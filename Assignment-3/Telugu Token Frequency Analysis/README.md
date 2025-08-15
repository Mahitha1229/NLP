# Telugu Token Frequency Analysis

## Overview
This project analyzes **Telugu text tokens** and visualizes the **Top 100 most frequent tokens** in a **horizontal bar chart**.  
It uses **Matplotlib** for visualization, **Counter** from Python's `collections` for frequency calculation, and a **custom Telugu font (.ttf)** to ensure proper rendering of Telugu characters.

---

## Files in This Project
- `Assignment_3_NLP_Frequency_Distributor.ipynb` → Main Jupyter Notebook containing markdown + code cells.
- `tokenized_telugu.txt` → Text file containing tokenized Telugu words (one or more per line).
- `NotoSansTelugu.ttf` (or other Telugu `.ttf` file) → Font file for proper Telugu text display.

---

## Requirements
Make sure you have the following installed:

```bash
pip install matplotlib pandas
```

## Data Preparation
1. Tokenized Telugu File

File named `tokenized_telugu.txt` must be present

2. Font Setup

To properly display Telugu text in plots, download a Telugu font file:

Recommended: Google Noto Sans Telugu

Direct .ttf download: NotoSansTelugu-Regular.ttf

Place the .ttf file in your project directory and update the path in the code:
`font_path = r"C:\path\to\NotoSansTelugu-Regular.ttf"`

`tokenized_telugu.txt` , `NotoSansTelugu-Regular.ttf` and `Assignment_3_NLP_Frequency_Distributor.ipynb` should be in the same folder




