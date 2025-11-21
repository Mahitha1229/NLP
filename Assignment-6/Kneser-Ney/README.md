# Kneser–Ney Quadrigram Model

This project implements the **Kneser–Ney smoothing algorithm** for quadrigrams (4‑grams).  
It reads a quadrigram count file (`quadrigram_model.txt`), computes smoothed probabilities for each quadrigram using Kneser–Ney, and saves the results into a CSV file.

---

## Project Structure
# Project folder structure

Kneser-Ney/
├── quadrigram_model.txt          # Input file containing quadrigram counts
├── kneser_ney.py                 # Python implementation of Kneser–Ney smoothing
├── quadgram_kneser_ney_output.csv # Output file with smoothed probabilities


---

## Input Format
The input file `quadrigram_model.txt` must contain one quadrigram per line:
 ```
అమెరికా అధ్యక్షుడు డొనాల్డ్ ట్రంప్	1
అధ్యక్షుడు డొనాల్డ్ ట్రంప్ కు	1
డొనాల్డ్ ట్రంప్ కు రాష్ట్రపతి	1

```


---

## How It Works
- **Counts loaded**: Quadrigram counts are read line by line to avoid memory overload.
- **Lower‑order counts derived**: Trigram, bigram, and unigram counts are computed automatically.
- **Continuation counts**: Tracks how often words appear in new contexts, a key feature of Kneser–Ney.
- **Absolute discounting**: Subtracts a fixed discount (default `0.75`) from observed counts.
- **Recursive backoff**:
  1. Quadrigram → Trigram → Bigram → Continuation Unigram.
  2. If denominator is zero, the model backs off immediately to avoid division errors.

---

## Usage
Run the script from the command line:

```bash
python kneser_ney.py
