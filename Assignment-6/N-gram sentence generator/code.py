import random
import heapq
from collections import Counter

# ---------------- NGram Sentence Generator ----------------
class NGramSentenceGenerator:
    def __init__(self, model, n=4):
        """
        model: an object with a .prob(w1,w2,w3,w4) method
        n: order of the n-gram (default=4 for quadrigram)
        """
        self.model = model
        self.n = n

    def greedy_generate(self, start_tokens, max_len=20):
        """
        Generate one sentence using greedy approach (MLE).
        """
        sentence = list(start_tokens)
        while len(sentence) < max_len:
            context = sentence[-(self.n-1):]  # last 3 words for quadrigram
            candidates = []
            for w in self.model.unigram_counts.keys():
                prob = self.model.prob(*context, w)
                candidates.append((prob, w))
            # pick word with max probability
            next_word = max(candidates, key=lambda x: x[0])[1]
            sentence.append(next_word)
            if next_word == "<END>":
                break
        return " ".join(sentence)

    def beam_search_generate(self, start_tokens, beam_size=20, max_len=20):
        """
        Generate one sentence using beam search.
        """
        beam = [(0.0, list(start_tokens))]  # (log_prob, sequence)
        for _ in range(max_len):
            new_beam = []
            for log_prob, seq in beam:
                context = seq[-(self.n-1):]
                for w in self.model.unigram_counts.keys():
                    prob = self.model.prob(*context, w)
                    if prob > 0:
                        new_seq = seq + [w]
                        # use -log(prob) for scoring
                        new_log_prob = log_prob + (-1 * (prob if prob > 0 else 1e-6))
                        new_beam.append((new_log_prob, new_seq))
            # keep top beam_size sequences
            if not new_beam:
                break
            beam = heapq.nsmallest(beam_size, new_beam, key=lambda x: x[0])
        # return best sequence
        best_seq = min(beam, key=lambda x: x[0])[1]
        return " ".join(best_seq)


# ---------------- Simple Kneser-Ney Quadgram ----------------
class KneserNeyQuadgram:
    def __init__(self, corpus, discount=0.75):
        """
        corpus: list of tokenized sentences (list of lists)
        discount: discount parameter for Kneser-Ney smoothing
        """
        self.discount = discount
        self.unigram_counts = Counter()
        self.bigram_counts = Counter()
        self.trigram_counts = Counter()
        self.quadgram_counts = Counter()

        # build counts
        for sentence in corpus:
            tokens = ["<START>", "<START>", "<START>"] + sentence + ["<END>"]
            for i in range(len(tokens)):
                self.unigram_counts[tokens[i]] += 1
                if i >= 1:
                    self.bigram_counts[(tokens[i-1], tokens[i])] += 1
                if i >= 2:
                    self.trigram_counts[(tokens[i-2], tokens[i-1], tokens[i])] += 1
                if i >= 3:
                    self.quadgram_counts[(tokens[i-3], tokens[i-2], tokens[i-1], tokens[i])] += 1

        self.total_unigrams = sum(self.unigram_counts.values())

    def prob(self, w1, w2, w3, w4):
        """
        Simplified Kneser-Ney probability for quadgrams.
        """
        quad = (w1, w2, w3, w4)
        trig = (w1, w2, w3)

        quad_count = self.quadgram_counts[quad]
        trig_count = self.trigram_counts[trig]

        if trig_count == 0:
            # back off to unigram probability
            return self.unigram_counts[w4] / self.total_unigrams

        # discounted probability
        return max(quad_count - self.discount, 0) / trig_count + \
               (self.discount / trig_count) * (self.unigram_counts[w4] / self.total_unigrams)


# ---------------- Load Corpus ----------------
def load_corpus(file_path):
    """
    Load corpus from a text file.
    Each line = one sentence.
    Returns: list of tokenized sentences (list of lists).
    """
    corpus = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            if tokens:
                corpus.append(tokens)
    return corpus


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    input_file = "quadrigram_model.txt"   # your corpus file
    corpus = load_corpus(input_file)

    model = KneserNeyQuadgram(corpus, discount=0.75)
    generator = NGramSentenceGenerator(model)

    print("Greedy Sentences:")
    for i in range(5):
        print(generator.greedy_generate(["<START>", "<START>", "<START>"], max_len=20))

    print("\nBeam Search Sentences:")
    for i in range(5):
        print(generator.beam_search_generate(["<START>", "<START>", "<START>"], beam_size=5, max_len=20))
