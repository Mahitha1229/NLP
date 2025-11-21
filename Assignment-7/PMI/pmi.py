#!/usr/bin/env python3
import math
from collections import Counter

# -----------------------------
# FILE NAMES (your files)
# -----------------------------
UNIGRAM_FILE = "inputs/unigram_model.txt"
BIGRAM_FILE  = "inputs/bigram_model.txt"
VAL_FILE     = "inputs/val.txt"
TEST_FILE    = "inputs/test.txt"
PMI_VAL_OUT = "outputs/pmi_val.txt"
PMI_TEST_OUT = "outputs/pmi_test.txt"


# -----------------------------
# Load models
# -----------------------------
def load_unigram_model(path):
    """
    Expects: token<TAB>value (count or probability)
    Returns: dict word -> P(word)
    """
    values = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                continue
            token, val_str = parts
            try:
                val = float(val_str)
            except ValueError:
                continue
            values[token] = val

    total = sum(values.values())
    # if it already looks like probabilities
    if 0.99 <= total <= 1.01:
        return values
    # otherwise normalize counts to probabilities
    return {w: c / total for w, c in values.items()}


def load_bigram_model(path):
    """
    Expects: 'w1 w2<TAB>value' (count or probability)
    Returns: dict (w1, w2) -> P(w1,w2)
    """
    values = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                continue
            bigram_str, val_str = parts
            words = bigram_str.split()
            if len(words) != 2:
                continue
            w1, w2 = words
            try:
                val = float(val_str)
            except ValueError:
                continue
            values[(w1, w2)] = val

    total = sum(values.values())
    if 0.99 <= total <= 1.01:
        return values
    return {(w1, w2): c / total for (w1, w2), c in values.items()}


# -----------------------------
# Read bigrams from corpus
# -----------------------------
def read_bigrams_from_corpus(path):
    """
    Reads val/test file (one sentence per line, whitespace tokenized).
    Returns Counter of bigrams (w1, w2) that appear in that file.
    """
    bigram_counts = Counter()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) < 2:
                continue
            for i in range(len(tokens) - 1):
                bigram = (tokens[i], tokens[i + 1])
                bigram_counts[bigram] += 1
    return bigram_counts


# -----------------------------
# Compute PMI
# -----------------------------
def compute_pmi_for_bigrams(bigram_counts, P_unigram, P_bigram):
    """
    bigram_counts: Counter[(w1, w2)] from val/test
    P_unigram: P(w)
    P_bigram: P(w1, w2)
    Returns dict: (w1, w2) -> PMI
    """
    pmi_scores = {}
    for (w1, w2), _ in bigram_counts.items():
        if (w1, w2) not in P_bigram:
            continue
        if w1 not in P_unigram or w2 not in P_unigram:
            continue

        p_w1w2 = P_bigram[(w1, w2)]
        p_w1 = P_unigram[w1]
        p_w2 = P_unigram[w2]

        denom = p_w1 * p_w2
        if denom <= 0 or p_w1w2 <= 0:
            continue

        pmi = math.log2(p_w1w2 / denom)
        pmi_scores[(w1, w2)] = pmi

    return pmi_scores


def write_pmi_to_file(pmi_scores, out_path):
    """
    Writes: 'w1 w2<TAB>PMI', sorted by descending PMI.
    """
    with open(out_path, "w", encoding="utf-8") as f:
        for (w1, w2), pmi in sorted(pmi_scores.items(), key=lambda x: -x[1]):
            f.write(f"{w1} {w2}\t{pmi:.6f}\n")


# -----------------------------
# Main
# -----------------------------
def main():
    print("Loading unigram and bigram models...")
    P_unigram = load_unigram_model(UNIGRAM_FILE)
    P_bigram = load_bigram_model(BIGRAM_FILE)

    # Validation / val.txt
    print("Reading bigrams from val.txt ...")
    val_bigrams = read_bigrams_from_corpus(VAL_FILE)
    print("Computing PMI for val bigrams...")
    val_pmi = compute_pmi_for_bigrams(val_bigrams, P_unigram, P_bigram)
    write_pmi_to_file(val_pmi, PMI_VAL_OUT)
    print(f"PMI for val written to {PMI_VAL_OUT}")

    # Test / test.txt
    print("Reading bigrams from test.txt ...")
    test_bigrams = read_bigrams_from_corpus(TEST_FILE)
    print("Computing PMI for test bigrams...")
    test_pmi = compute_pmi_for_bigrams(test_bigrams, P_unigram, P_bigram)
    write_pmi_to_file(test_pmi, PMI_TEST_OUT)
    print(f"PMI for test written to {PMI_TEST_OUT}")


if __name__ == "__main__":
    main()
