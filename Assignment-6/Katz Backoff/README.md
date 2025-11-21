# Katz Backoff Quadrigram Processor

This project implements a Katz Backoff language model for quadrigrams and generates a CSV file containing the Katz Backoff probabilities for each entry in a quadrigram dataset.

The program streams the quadrigram file line-by-line, making it suitable for very large datasets that cannot fit entirely into memory.

------------------------------------------------------------
FEATURES
------------------------------------------------------------
- Computes Katz Backoff probabilities for quadrigrams.
- Streams input file to avoid memory overload.
- Automatically extracts trigram, bigram, and unigram counts.
- Saves output as a CSV file.
- Supports custom discount (default: 0.75).
- No external dependencies required.

------------------------------------------------------------
INPUT FILE FORMAT
------------------------------------------------------------
The input file (quadrigram_model.txt) must contain lines of the form:

w1 w2 w3 w4 count

Example:
the quick brown fox 12
quick brown fox jumps 5
brown fox jumps over 7

------------------------------------------------------------
OUTPUT
------------------------------------------------------------
The script creates a CSV file:

quadgram_katz_output.csv

Columns:
w1, w2, w3, w4, count, katz_backoff_prob

Example row:
the, quick, brown, fox, 12, 0.00453121

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------
quadrigram_model.txt        # input file
quadgram_katz_output.csv    # generated output
katz_quadgram.py            # your script

------------------------------------------------------------
USAGE
------------------------------------------------------------
1. Ensure quadrigram_model.txt exists in the same directory.
2. Run the script:

    python katz_quadgram.py

3. Output will be written to:

    quadgram_katz_output.csv

------------------------------------------------------------
HOW THE KATZ BACKOFF WORKS (SIMPLIFIED)
------------------------------------------------------------
The probability of (w1, w2, w3, w4) is computed using 4 levels:

1. Quadrigram exists:
   P = (count_quad - discount) / count_trigram

2. Otherwise back off to trigram:
   P = (count_trigram - discount) / count_bigram

3. Otherwise back off to bigram:
   P = (count_bigram - discount) / count_unigram

4. Otherwise fall back to unigram:
   P = count(w4) / total_unigram_count

This approach redistributes probability mass from seen n-grams to unseen ones.

------------------------------------------------------------
CUSTOM DISCOUNT
------------------------------------------------------------
You can set a different discount:

process_quadgram_file("quadrigram_model.txt",
                      "quadgram_katz_output.csv",
                      discount=0.5)

Typical range: 0.5 – 1.0

------------------------------------------------------------
EXAMPLE PROGRAMMATIC USAGE
------------------------------------------------------------
model = KatzBackoffQuadgram("quadrigram_model.txt", discount=0.75)
p = model.prob("the", "quick", "brown", "fox")
print(p)

------------------------------------------------------------
NOTES
------------------------------------------------------------
- Unigram counts are approximated by summing all token occurrences in quadrigrams.
- Designed for large datasets, minimalist and efficient.


