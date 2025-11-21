# N-Gram Sentence Generator (Quadgram with Kneser-Ney Smoothing)

## Overview
This project implements a sentence generator using n-gram language models.  
Specifically, it uses a Quadgram (4-gram) model with Kneser-Ney smoothing to estimate probabilities of word sequences.  

Two generation strategies are supported:
1. Greedy Approach (Maximum Likelihood Estimation)  
   - At each step, the most probable next word is chosen.
2. Beam Search (beam size = 20)  
   - Multiple candidate sequences are explored in parallel, keeping the top `beam_size` sequences at each step.

---

## Project Structure
- `code.py` → Main implementation (sentence generator + Kneser-Ney model).
- `quadrigram_model.txt` → Input corpus file (each line = one sentence).
- `generated_sentences.txt` → Output file (generated sentences will be stored here if you extend the code).

---

## Requirements
- Python 3.7+
- No external libraries required (uses only built-in modules: `random`, `heapq`, `collections`).

---

## How to Run
1. Place your corpus file named `quadrigram_model.txt` in the same directory as `code.py`.  
   - Each line should contain one sentence (tokens separated by spaces).
   

2. Run the script:
```
python code.py
```

3. The program will:
- Load the corpus.
- Train a Quadgram model with Kneser-Ney smoothing.
- Generate sentences using:
  - Greedy approach (prints sentences).
  - Beam search (prints sentences).

---

##  Example Output

```
<START> <START> <START> ‌ లో ఈ 1 <END> <END> <START> <START> <END> <START> <START> <END> <START> <START> <END> <START>   <START> <END> <START> <START>
<START> <START> <START> ‌ లో ఈ 1 <END> <END> <START> <START> <END> <START> <START> <END> <START> <START> <END> <START>   <START> <END> <START> <START>

```

---

## Notes
- You can adjust:
  - `max_len` → maximum sentence length.
  - `beam_size` → number of candidate sequences kept during beam search.
  - Number of sentences generated (currently set to 5 for each method).
- For assignment requirements, change the loops to generate 100 sentences instead of 5.


