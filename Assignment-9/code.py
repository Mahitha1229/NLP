import collections

# ============================================================
# Helper: Load corpus as word -> frequency
# ============================================================

def load_corpus_words(path):
    """
    Reads a corpus file (your tokenized_telugu.txt) where each line
    is a tokenized sentence (tokens separated by spaces).

    Returns:
        dict: {word: frequency}
    """
    freqs = collections.Counter()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            if not tokens:
                continue
            freqs.update(tokens)
    return dict(freqs)


def word_to_symbols(word, eow="</w>"):
    """
    Represent a word as list of characters + end-of-word symbol.
    Example: 'hello' -> ['h', 'e', 'l', 'l', 'o', '</w>']
    """
    return list(word) + [eow]


# ============================================================
# BPE IMPLEMENTATION
# ============================================================

def get_pair_stats_bpe(word_freqs):
    """
    word_freqs: dict {tuple(symbols): freq}
    Returns:
        pair_stats: dict {(sym1, sym2): total_count}
    """
    pair_stats = collections.Counter()
    for symbols, freq in word_freqs.items():
        if len(symbols) < 2:
            continue
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pair_stats[pair] += freq
    return pair_stats


def merge_pair_in_words(pair, word_freqs):
    """
    Given pair (A, B), merges all occurrences of "A B" into "AB"
    in all words (represented as tuples of symbols).

    Returns new dict {tuple(symbols): freq}
    """
    new_word_freqs = {}
    merged_symbol = "".join(pair)

    for symbols, freq in word_freqs.items():
        new_symbols = []
        i = 0
        while i < len(symbols):
            if (
                i < len(symbols) - 1
                and symbols[i] == pair[0]
                and symbols[i + 1] == pair[1]
            ):
                new_symbols.append(merged_symbol)
                i += 2
            else:
                new_symbols.append(symbols[i])
                i += 1
        new_symbols = tuple(new_symbols)
        new_word_freqs[new_symbols] = new_word_freqs.get(new_symbols, 0) + freq

    return new_word_freqs


def learn_bpe(corpus_path, num_merges=None, target_vocab_size=None, eow="</w>"):
    """
    Learn BPE merges from corpus.

    Parameters:
        corpus_path (str): path to corpus file (tokenized_telugu.txt)
        num_merges (int or None): number of merge steps (setting a)
        target_vocab_size (int or None): stop when vocab size reaches this (setting b)
        eow (str): end-of-word symbol

    Returns:
        merges (list of (sym1, sym2))
        vocab (set of symbols)
    """
    if num_merges is None and target_vocab_size is None:
        raise ValueError("Provide either num_merges or target_vocab_size for BPE.")

    # 1. Load word frequencies
    word_counts_word = load_corpus_words(corpus_path)

    # 2. Represent each word as sequence of symbols (chars + </w>)
    word_freqs = {}
    for w, c in word_counts_word.items():
        symbols = tuple(word_to_symbols(w, eow=eow))
        word_freqs[symbols] = word_freqs.get(symbols, 0) + c

    # 3. Initial vocab = all symbols
    vocab = set()
    for symbols in word_freqs.keys():
        vocab.update(symbols)

    merges = []
    step = 0

    while True:
        # Stop conditions
        if num_merges is not None and step >= num_merges:
            break
        if target_vocab_size is not None and len(vocab) >= target_vocab_size:
            break

        # 4. Count pair frequencies
        pair_stats = get_pair_stats_bpe(word_freqs)
        if not pair_stats:
            break

        # 5. Find most frequent pair
        best_pair, best_count = max(pair_stats.items(), key=lambda x: x[1])
        if best_count < 1:
            break

        merges.append(best_pair)

        # 6. Merge this pair in all words
        word_freqs = merge_pair_in_words(best_pair, word_freqs)

        # 7. Update vocab
        merged_symbol = "".join(best_pair)
        vocab.add(merged_symbol)

        step += 1
        if step % 1000 == 0:
            print(f"[BPE] step {step}, vocab size {len(vocab)}")

    return merges, vocab


# ============================================================
# WORDPIECE IMPLEMENTATION
# ============================================================

def get_token_and_pair_stats_wp(sequences, seq_freqs):
    """
    WordPiece helper:

    sequences: list of tuple(tokens)
    seq_freqs: list of frequencies for each sequence

    Returns:
        token_freq: dict token -> usage count
        pair_freq: dict (t1, t2) -> usage count
    """
    token_freq = collections.Counter()
    pair_freq = collections.Counter()

    for symbols, freq in zip(sequences, seq_freqs):
        for s in symbols:
            token_freq[s] += freq
        if len(symbols) > 1:
            for i in range(len(symbols) - 1):
                pair = (symbols[i], symbols[i + 1])
                pair_freq[pair] += freq

    return token_freq, pair_freq


def merge_pair_in_sequences_wp(pair, sequences):
    """
    Merge pair (A, B) into "AB" in all sequences (for WordPiece).
    """
    merged_symbol = "".join(pair)
    new_sequences = []

    for symbols in sequences:
        new_symbols = []
        i = 0
        while i < len(symbols):
            if (
                i < len(symbols) - 1
                and symbols[i] == pair[0]
                and symbols[i + 1] == pair[1]
            ):
                new_symbols.append(merged_symbol)
                i += 2
            else:
                new_symbols.append(symbols[i])
                i += 1
        new_sequences.append(tuple(new_symbols))

    return new_sequences


def learn_wordpiece(corpus_path, num_merges=None, target_vocab_size=None, eow="</w>"):
    """
    Simple WordPiece-style vocab learning from scratch.

    Algorithm sketch:
      - Initialize with character-level tokens + </w>
      - Repeatedly:
         * compute token_freq and pair_freq over all sequences
         * compute score(pair) = pair_freq / (token_freq[left] * token_freq[right])
         * merge the pair with highest score
      - Stop after num_merges steps or when vocab size reaches target_vocab_size.

    Parameters:
        corpus_path (str): path to corpus file
        num_merges (int or None)
        target_vocab_size (int or None)
        eow (str): end-of-word symbol

    Returns:
        merges (list of (sym1, sym2))
        vocab (set of tokens)
    """
    if num_merges is None and target_vocab_size is None:
        raise ValueError("Provide either num_merges or target_vocab_size for WordPiece.")

    # 1. Load word frequencies
    word_counts_word = load_corpus_words(corpus_path)

    # 2. Represent each word as sequence of initial tokens (chars + </w>)
    sequences = []
    seq_freqs = []
    for w, c in word_counts_word.items():
        symbols = tuple(word_to_symbols(w, eow=eow))
        sequences.append(symbols)
        seq_freqs.append(c)

    # 3. Initial vocab
    vocab = set()
    for seq in sequences:
        vocab.update(seq)

    merges = []
    step = 0

    while True:
        if num_merges is not None and step >= num_merges:
            break
        if target_vocab_size is not None and len(vocab) >= target_vocab_size:
            break

        token_freq, pair_freq = get_token_and_pair_stats_wp(sequences, seq_freqs)
        if not pair_freq:
            break

        # 4. Compute WordPiece scores for each pair
        best_pair = None
        best_score = -1.0

        for pair, pf in pair_freq.items():
            left, right = pair
            # Avoid division by zero
            if token_freq[left] == 0 or token_freq[right] == 0:
                continue
            score = pf / (token_freq[left] * token_freq[right])
            if score > best_score:
                best_score = score
                best_pair = pair

        if best_pair is None:
            break

        merges.append(best_pair)

        # 5. Merge best pair in all sequences
        sequences = merge_pair_in_sequences_wp(best_pair, sequences)

        merged_symbol = "".join(best_pair)
        vocab.add(merged_symbol)

        step += 1
        if step % 1000 == 0:
            print(f"[WordPiece] step {step}, vocab size {len(vocab)}")

    return merges, vocab


# ============================================================
# MAIN: run all required settings on tokenized_telugu.txt
# ============================================================

if __name__ == "__main__":
    corpus_file = "tokenized_telugu.txt"   # your input file

    # ---------- BPE (a) 32000 merge steps ----------
    print("Training BPE with 32000 merge steps...")
    bpe_merges_32000, bpe_vocab_32000 = learn_bpe(
        corpus_file,
        num_merges=32000,
        target_vocab_size=None
    )

    with open("bpe_merges_32000.txt", "w", encoding="utf-8") as f:
        for a, b in bpe_merges_32000:
            f.write(f"{a} {b}\n")

    with open("bpe_vocab_32000.txt", "w", encoding="utf-8") as f:
        for tok in sorted(bpe_vocab_32000):
            f.write(tok + "\n")

    # ---------- BPE (b) vocab size = 32000 ----------
    print("Training BPE with target vocab size 32000...")
    bpe_merges_vocab32000, bpe_vocab_by_size = learn_bpe(
        corpus_file,
        num_merges=None,
        target_vocab_size=32000
    )

    with open("bpe_merges_vocab32000.txt", "w", encoding="utf-8") as f:
        for a, b in bpe_merges_vocab32000:
            f.write(f"{a} {b}\n")

    with open("bpe_vocab_32000_by_size.txt", "w", encoding="utf-8") as f:
        for tok in sorted(bpe_vocab_by_size):
            f.write(tok + "\n")

    # ---------- WordPiece (vocab size = 32000) ----------
    print("Training WordPiece with target vocab size 32000...")
    wp_merges_vocab32000, wp_vocab_32000 = learn_wordpiece(
        corpus_file,
        num_merges=None,
        target_vocab_size=32000
    )

    with open("wordpiece_merges_vocab32000.txt", "w", encoding="utf-8") as f:
        for a, b in wp_merges_vocab32000:
            f.write(f"{a} {b}\n")

    with open("wordpiece_vocab_32000.txt", "w", encoding="utf-8") as f:
        for tok in sorted(wp_vocab_32000):
            f.write(tok + "\n")

    print("Done. All vocab and merge files written.")
