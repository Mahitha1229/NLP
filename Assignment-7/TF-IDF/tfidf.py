import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import save_npz

# ==============================
# CONFIG – change filenames if needed
# ==============================
TRAIN_FILE = "inputs/train.txt"
VAL_FILE   = "inputs/val.txt"
TEST_FILE  = "inputs/test.txt"

OUT_DIR = "outputs/tfidf_output"   # folder to save matrices + vocab


def read_sentences(path):
    """
    Reads a text file with one sentence per line.
    Assumes sentences are already tokenized (tokens separated by spaces).
    Returns: list of strings.
    """
    sentences = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sentences.append(line)
    return sentences


def main():
    # create output directory if not exists
    Path(OUT_DIR).mkdir(exist_ok=True)

    print("Reading data...")
    train_sents = read_sentences(TRAIN_FILE)
    val_sents   = read_sentences(VAL_FILE)
    test_sents  = read_sentences(TEST_FILE)

    print(f"# train sentences: {len(train_sents)}")
    print(f"# val   sentences: {len(val_sents)}")
    print(f"# test  sentences: {len(test_sents)}")

    # ==============================
    # TF-IDF: fit on TRAIN ONLY
    # ==============================
    # tokenizer=str.split: use your existing tokenization (space-separated)
    vectorizer = TfidfVectorizer(
        analyzer="word",
        tokenizer=str.split,  # don't re-tokenize; just split on spaces
        preprocessor=None,
        token_pattern=None,   # required when using custom tokenizer
    )

    print("\nFitting TF-IDF on TRAIN (learning IDF from train only)...")
    X_train = vectorizer.fit_transform(train_sents)

    print("Transforming VAL and TEST using train IDF...")
    X_val = vectorizer.transform(val_sents)
    X_test = vectorizer.transform(test_sents)

    # ==============================
    # Save outputs
    # ==============================
    print("\nSaving sparse TF-IDF matrices...")
    save_npz(Path(OUT_DIR) / "tfidf_train.npz", X_train)
    save_npz(Path(OUT_DIR) / "tfidf_val.npz", X_val)
    save_npz(Path(OUT_DIR) / "tfidf_test.npz", X_test)

    print("Saving vocabulary (token -> column index)...")
    vocab = vectorizer.vocabulary_  # dict[token] = column_index
    with open(Path(OUT_DIR) / "vocab.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    print("\nDone!")
    print(f"Train TF-IDF shape: {X_train.shape}")
    print(f"Val   TF-IDF shape: {X_val.shape}")
    print(f"Test  TF-IDF shape: {X_test.shape}")


if __name__ == "__main__":
    main()
