import numpy as np
from pathlib import Path

from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# CONFIG – change paths if needed
# ==============================
TRAIN_SENT_FILE = "inputs/train.txt"
VAL_SENT_FILE   = "inputs/val.txt"
TEST_SENT_FILE  = "inputs/test.txt"

TRAIN_TFIDF_FILE = "inputs/tfidf_train.npz"
VAL_TFIDF_FILE   = "inputs/tfidf_val.npz"
TEST_TFIDF_FILE  = "inputs/tfidf_test.npz"

OUT_VAL_NEIGHBORS_TRAIN  = "outputs/nearest_neighbors_val_in_train.txt"
OUT_TEST_NEIGHBORS_TRAIN = "outputs/nearest_neighbors_test_in_train.txt"

# for memory safety if train is big
BATCH_SIZE = 500   # number of queries to process at once


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


def find_nearest_neighbors_in_train(X_queries, X_train, batch_size=500):
    """
    X_queries: sparse matrix, shape (n_queries, d)
    X_train:   sparse matrix, shape (n_train, d)
    For each query sentence q, find index t in train with max cosine similarity.
    Uses batching to avoid huge memory for cosine_similarity.
    Returns: list of (q_index, train_index, sim)
    """
    n_queries = X_queries.shape[0]
    n_train = X_train.shape[0]

    neighbors = []

    start = 0
    while start < n_queries:
        end = min(start + batch_size, n_queries)
        X_batch = X_queries[start:end]

        # cosine_similarity between batch (queries) and all train sentences
        sims = cosine_similarity(X_batch, X_train)   # shape: (batch_size, n_train)

        # for each query in the batch, pick argmax over train indices
        batch_size_actual = sims.shape[0]
        for i in range(batch_size_actual):
            j = int(np.argmax(sims[i]))
            sim_ij = float(sims[i, j])
            q_index = start + i
            neighbors.append((q_index, j, sim_ij))

        start = end

    return neighbors


def write_neighbors(out_path, query_sents, train_sents, neighbors):
    """
    Writes nearest neighbor info.
    Format per line:
    q_index<TAB>train_index<TAB>similarity<TAB>query_sentence<TAB>|||<TAB>train_sentence
    """
    with open(out_path, "w", encoding="utf-8") as f:
        for qi, ti, sim_ij in neighbors:
            q_sent = query_sents[qi]
            t_sent = train_sents[ti]
            f.write(f"{qi}\t{ti}\t{sim_ij:.4f}\t{q_sent}\t|||\t{t_sent}\n")


def estimate_operations(n_queries, n_train, dim):
    """
    Rough estimate of operations for dense dot products:
        ops ≈ n_queries * n_train * dim
    (Each dot product of length dim ~ dim multiplications + additions)
    """
    return n_queries * n_train * dim


def main():
    # ==============================
    # Load sentences
    # ==============================
    print("Loading sentences...")
    train_sents = read_sentences(TRAIN_SENT_FILE)
    val_sents   = read_sentences(VAL_SENT_FILE)
    test_sents  = read_sentences(TEST_SENT_FILE)

    # ==============================
    # Load TF-IDF matrices
    # ==============================
    print("Loading TF-IDF matrices...")
    X_train = load_npz(TRAIN_TFIDF_FILE)
    X_val   = load_npz(VAL_TFIDF_FILE)
    X_test  = load_npz(TEST_TFIDF_FILE)

    print(f"Train TF-IDF shape: {X_train.shape}")
    print(f"Val   TF-IDF shape: {X_val.shape}")
    print(f"Test  TF-IDF shape: {X_test.shape}")

    # sanity checks
    if X_train.shape[0] != len(train_sents):
        print("WARNING: #rows in tfidf_train.npz does not match #lines in train.txt")
    if X_val.shape[0] != len(val_sents):
        print("WARNING: #rows in tfidf_val.npz does not match #lines in val.txt")
    if X_test.shape[0] != len(test_sents):
        print("WARNING: #rows in tfidf_test.npz does not match #lines in test.txt")

    dim = X_train.shape[1]

    # ==============================
    # VAL -> TRAIN (nearest neighbor)
    # ==============================
    print("\nFinding nearest neighbors: VAL sentences in TRAIN set...")
    val_neighbors = find_nearest_neighbors_in_train(X_val, X_train, batch_size=BATCH_SIZE)
    write_neighbors(OUT_VAL_NEIGHBORS_TRAIN, val_sents, train_sents, val_neighbors)
    print(f"Validation->Train neighbors written to {OUT_VAL_NEIGHBORS_TRAIN}")

    # estimate operations for val->train
    ops_val_train = estimate_operations(X_val.shape[0], X_train.shape[0], dim)
    print(f"Approx. operations for VAL->TRAIN (dense dot products): {ops_val_train:e}")

    # ==============================
    # TEST -> TRAIN (nearest neighbor)
    # ==============================
    print("\nFinding nearest neighbors: TEST sentences in TRAIN set...")
    test_neighbors = find_nearest_neighbors_in_train(X_test, X_train, batch_size=BATCH_SIZE)
    write_neighbors(OUT_TEST_NEIGHBORS_TRAIN, test_sents, train_sents, test_neighbors)
    print(f"Test->Train neighbors written to {OUT_TEST_NEIGHBORS_TRAIN}")

    # estimate operations for test->train
    ops_test_train = estimate_operations(X_test.shape[0], X_train.shape[0], dim)
    print(f"Approx. operations for TEST->TRAIN (dense dot products): {ops_test_train:e}")

    # ==============================
    # Summary for your report
    # ==============================
    print("\nSummary:")
    print(f"  #train sentences: {X_train.shape[0]}")
    print(f"  #val   sentences: {X_val.shape[0]}")
    print(f"  #test  sentences: {X_test.shape[0]}")
    print(f"  TF-IDF dimension: {dim}")
    print(f"  Estimated ops VAL->TRAIN  ≈ N_val * N_train * D  = {ops_val_train:e}")
    print(f"  Estimated ops TEST->TRAIN ≈ N_test * N_train * D = {ops_test_train:e}")
    print("\nDone!")


if __name__ == "__main__":
    main()
