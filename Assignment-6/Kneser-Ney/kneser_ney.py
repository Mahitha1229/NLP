import csv
from collections import defaultdict

class KneserNeyQuadgram:
    def __init__(self, quadgram_file, discount=0.75):
        """
        Kneser-Ney smoothing for quadrigrams.
        quadgram_file: path to quadrigram_model.txt (format: w1 w2 w3 w4 count)
        discount: absolute discount (usually 0.75)
        """
        self.discount = discount
        self.quadgram_counts = defaultdict(int)
        self.trigram_counts = defaultdict(int)
        self.bigram_counts = defaultdict(int)
        self.unigram_counts = defaultdict(int)

        # Continuation counts (for Kneser-Ney)
        self.word_continuation = defaultdict(set)
        self.bigram_continuation = defaultdict(set)
        self.trigram_continuation = defaultdict(set)

        self.total_unigrams = 0
        self._load_quadgrams(quadgram_file)

    def _load_quadgrams(self, filepath):
        """Load quadrigram counts and derive lower-order counts + continuation sets."""
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                w1, w2, w3, w4, count = parts
                count = int(count)

                # Store quadgram
                self.quadgram_counts[(w1, w2, w3, w4)] += count

                # Lower-order counts
                self.trigram_counts[(w1, w2, w3)] += count
                self.bigram_counts[(w2, w3)] += count
                self.unigram_counts[w4] += count
                self.total_unigrams += count

                # Continuation sets
                self.word_continuation[w4].add((w1, w2, w3))
                self.bigram_continuation[(w3, w4)].add((w1, w2))
                self.trigram_continuation[(w2, w3, w4)].add(w1)

    def continuation_prob(self, word):
        """Continuation probability for unigram (Kneser-Ney)."""
        if len(self.quadgram_counts) == 0:
            return 1e-6
        return len(self.word_continuation[word]) / len(self.quadgram_counts)

    def prob(self, w1, w2, w3, w4):
        """Compute Kneser-Ney probability for quadrigram (w1,w2,w3,w4)."""
        quad = (w1, w2, w3, w4)
        tri = (w1, w2, w3)

        denominator = self.trigram_counts[tri]
        if denominator > 0 and self.quadgram_counts[quad] > 0:
            numerator = max(self.quadgram_counts[quad] - self.discount, 0)
            lambda_weight = (self.discount / denominator) * len(self.trigram_continuation[(w1, w2, w3, w4)])
            return (numerator / denominator) + lambda_weight * self.prob_trigram(w2, w3, w4)
        else:
            return self.prob_trigram(w2, w3, w4)

    def prob_trigram(self, w2, w3, w4):
        tri = (w2, w3, w4)
        bi = (w2, w3)

        denominator = self.bigram_counts[bi]
        if denominator > 0 and self.trigram_counts[tri] > 0:
            numerator = max(self.trigram_counts[tri] - self.discount, 0)
            lambda_weight = (self.discount / denominator) * len(self.bigram_continuation[(w3, w4)])
            return (numerator / denominator) + lambda_weight * self.prob_bigram(w3, w4)
        else:
            return self.prob_bigram(w3, w4)

    def prob_bigram(self, w3, w4):
        bi = (w3, w4)
        denominator = self.unigram_counts[w3]

        if denominator > 0 and self.bigram_counts[bi] > 0:
            numerator = max(self.bigram_counts[bi] - self.discount, 0)
            lambda_weight = (self.discount / denominator) * len(self.word_continuation[w4])
            return (numerator / denominator) + lambda_weight * self.continuation_prob(w4)
        else:
            return self.continuation_prob(w4)


def process_quadgram_file(input_file, output_file, discount=0.75):
    """
    Process the entire quadrigram file and save Kneser-Ney probabilities to CSV.
    """
    model = KneserNeyQuadgram(input_file, discount)

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        writer = csv.writer(outfile)
        writer.writerow(["w1", "w2", "w3", "w4", "count", "kneser_ney_prob"])

        for line in infile:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            w1, w2, w3, w4, count = parts
            prob_value = model.prob(w1, w2, w3, w4)
            writer.writerow([w1, w2, w3, w4, count, f"{prob_value:.8f}"])


if __name__ == "__main__":
    input_path = "quadrigram_model.txt"
    output_path = "quadgram_kneser_ney_output.csv"

    process_quadgram_file(input_path, output_path, discount=0.75)
    print(f"Processing complete. Results saved to {output_path}")