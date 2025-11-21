import numpy as np
from pathlib import Path

from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# CONFIG – change paths if needed
# ==============================
VAL_SENT_FILE = "inputs/val.txt"
TEST_SENT_FILE = "inputs/test.txt"

VAL_TFIDF_FILE = "inputs/tfidf_val.npz"
TEST_TFIDF_FILE = "inputs/tfidf_test.npz"

OUT_VAL_NEIGHBORS  = "outputs/nearest_neighbors_val.txt"
OUT_TEST_NEIGHBORS = "outputs/nearest_neighbors_test.txt"


def read_sentences(path):
    """
    Reads one sentence per line.
    Returns: list of strings.
    """
    sents = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sents.append(line)
    return sents


def find_nearest_neighbors(X):
    """
    X: sparse TF-IDF matrix of shape (n_sentences, n_features)
    For each sentence i, find index j != i with maximum cosine similarity.
    Returns: list of (i, j, sim_ij)
    """
    n = X.shape[0]
    neighbors = []

    for i in range(n):
        # cosine_similarity between sentence i and all sentences
        sims = cosine_similarity(X[i], X).flatten()   # shape: (n,)
        sims[i] = -1.0  # exclude self

        j = int(np.argmax(sims))
        sim_ij = float(sims[j])
        neighbors.append((i, j, sim_ij))

    return neighbors


def write_neighbors(out_path, sentences, neighbors):
    """
    Writes nearest neighbor info.
    Format per line:
    sent_index<TAB>neighbor_index<TAB>similarity<TAB>sentence<TAB>|||<TAB>neighbor_sentence
    """
    with open(out_path, "w", encoding="utf-8") as f:
        for i, j, sim_ij in neighbors:
            s_i = sentences[i]
            s_j = sentences[j]
            f.write(f"{i}\t{j}\t{sim_ij:.4f}\t{s_i}\t|||\t{s_j}\n")


def main():
    # ==============================
    # VALIDATION SET
    # ==============================
    print("Loading validation sentences and TF-IDF matrix...")
    val_sents = read_sentences(VAL_SENT_FILE)
    X_val = load_npz(VAL_TFIDF_FILE)

    if X_val.shape[0] != len(val_sents):
        print("WARNING: #rows in tfidf_val.npz does not match #lines in val.txt")

    print("Finding nearest neighbors in validation set...")
    val_neighbors = find_nearest_neighbors(X_val)

    print(f"Writing validation nearest neighbors to {OUT_VAL_NEIGHBORS} ...")
    write_neighbors(OUT_VAL_NEIGHBORS, val_sents, val_neighbors)

    # ==============================
    # TEST SET
    # ==============================
    print("Loading test sentences and TF-IDF matrix...")
    test_sents = read_sentences(TEST_SENT_FILE)
    X_test = load_npz(TEST_TFIDF_FILE)

    if X_test.shape[0] != len(test_sents):
        print("WARNING: #rows in tfidf_test.npz does not match #lines in test.txt")

    print("Finding nearest neighbors in test set...")
    test_neighbors = find_nearest_neighbors(X_test)

    print(f"Writing test nearest neighbors to {OUT_TEST_NEIGHBORS} ...")
    write_neighbors(OUT_TEST_NEIGHBORS, test_sents, test_neighbors)

    print("\nDone!")
    print(f"Validation sentences: {len(val_sents)}")
    print(f"Test sentences:       {len(test_sents)}")


if __name__ == "__main__":
    main()
