import re
import math
from collections import Counter, defaultdict

# ---------------- Preprocessing ----------------
def preprocess(sentence):
    """
    Preprocess a sentence:
    a. Tokenize
    b. Replace numbers with NUMBER
    c. Replace URLs with URL
    d. Replace punctuation with PUNCT
    e. Lowercase everything
    """
    # Lowercase
    sentence = sentence.lower()

    # Replace URLs
    sentence = re.sub(r'http\S+|www\.\S+', 'URL', sentence)

    # Replace numbers
    sentence = re.sub(r'\d+', 'NUMBER', sentence)

    # Replace punctuation with PUNCT
    sentence = re.sub(r'[^\w\s]', ' PUNCT ', sentence)

    # Tokenize (split by whitespace)
    tokens = sentence.split()

    return tokens


# ---------------- Term Frequency ----------------
def compute_tf_with_normalization(sentence_tokens, vocab, smoothing=False):
    """
    Compute term frequency with normalization.
    TF = log(1 + count(term)) / total terms
    If smoothing=True, apply add-one smoothing.
    """
    tf_scores = {}
    term_counts = Counter(sentence_tokens)
    total_terms = len(sentence_tokens)

    for term in vocab:
        count = term_counts[term]
        if smoothing:
            # add-one smoothing
            count += 1
            total_terms += len(vocab)
        tf_scores[term] = math.log(1 + count) / total_terms if total_terms > 0 else 0.0

    return tf_scores


# ---------------- Inverse Document Frequency ----------------
def compute_idf(sentences_tokens, vocab, smoothing=False):
    """
    Compute IDF for each term.
    IDF = log(N / df(term))
    If smoothing=True, use add-one smoothing.
    """
    idf_scores = {}
    N = len(sentences_tokens)

    # document frequency
    df = defaultdict(int)
    for tokens in sentences_tokens:
        unique_terms = set(tokens)
        for term in unique_terms:
            df[term] += 1

    for term in vocab:
        if smoothing:
            idf_scores[term] = math.log((N + 1) / (df[term] + 1))
        else:
            if df[term] > 0:
                idf_scores[term] = math.log(N / df[term])
            else:
                idf_scores[term] = 0.0

    return idf_scores


# ---------------- TF-IDF ----------------
def compute_tf_idf_scores(sentences_tokens, smoothing=False):
    """
    Compute TF-IDF scores for all sentences.
    """
    # Build vocabulary
    vocab = set(term for tokens in sentences_tokens for term in tokens)

    # Compute IDF
    idf_scores = compute_idf(sentences_tokens, vocab, smoothing=smoothing)

    # Compute TF-IDF for each sentence
    tf_idf_all = []
    for tokens in sentences_tokens:
        tf_scores = compute_tf_with_normalization(tokens, vocab, smoothing=smoothing)
        tf_idf = {term: tf_scores[term] * idf_scores[term] for term in vocab}
        tf_idf_all.append(tf_idf)

    return tf_idf_all


# ---------------- Main ----------------
def main():
    sentences = [
        "The cat sat on the mat.",
        "Visit https://example.com for more info!",
        "There are 123 apples in the basket.",
        "Hello, world!!!",
    ]

    # Preprocess
    sentences_tokens = [preprocess(s) for s in sentences]

    # Print and save outputs
    with open("tfidf_output.txt", "w", encoding="utf-8") as out:
        out.write("Preprocessed Sentences:\n")
        for s, tokens in zip(sentences, sentences_tokens):
            line = f"{s} -> {tokens}"
            print(line)
            out.write(line + "\n")

        # Compute TF-IDF
        tf_idf_scores = compute_tf_idf_scores(sentences_tokens, smoothing=True)

        out.write("\nTF-IDF Scores:\n")
        print("\nTF-IDF Scores:")
        for i, tfidf in enumerate(tf_idf_scores):
            header = f"Sentence {i+1}:"
            print(header)
            out.write(header + "\n")
            for term, score in tfidf.items():
                line = f"  {term}: {score:.4f}"
                print(line)
                out.write(line + "\n")

    print("\nOutput saved to tfidf_output.txt")


if __name__ == "__main__":
    main()
