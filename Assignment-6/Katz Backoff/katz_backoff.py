import csv
from collections import defaultdict

class KatzBackoffQuadgram:
    def __init__(self, quadgram_file, discount=0.75):
        """
        Katz Backoff model for quadrigrams.
        quadgram_file: path to quadrigram_model.txt (format: w1 w2 w3 w4 count)
        discount: discount factor (usually 0.5–1.0)
        """
        self.discount = discount
        self.quadgram_counts = defaultdict(int)
        self.trigram_counts = defaultdict(int)
        self.bigram_counts = defaultdict(int)
        self.unigram_counts = defaultdict(int)
        self.total_unigrams = 0

        self._stream_load_quadgrams(quadgram_file)

    def _stream_load_quadgrams(self, filepath):
        """Stream through quadrigram file line by line to avoid memory overload."""
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                w1, w2, w3, w4, count = parts
                count = int(count)

                # Store quadgram
                self.quadgram_counts[(w1, w2, w3, w4)] += count

                # Derive lower-order counts
                self.trigram_counts[(w1, w2, w3)] += count
                self.bigram_counts[(w2, w3)] += count
                self.unigram_counts[w1] += count
                self.unigram_counts[w2] += count
                self.unigram_counts[w3] += count
                self.unigram_counts[w4] += count
                self.total_unigrams += count

    def prob(self, w1, w2, w3, w4):
        """Compute Katz Backoff probability for quadrigram (w1,w2,w3,w4)."""
        quad = (w1, w2, w3, w4)
        tri = (w1, w2, w3)
        bi = (w2, w3)
        uni = w3

        # Case 1: quadrigram exists
        if self.quadgram_counts[quad] > 0:
            return max(self.quadgram_counts[quad] - self.discount, 0) / self.trigram_counts[tri]

        # Case 2: backoff to trigram
        if self.trigram_counts[(w2, w3, w4)] > 0:
            return max(self.trigram_counts[(w2, w3, w4)] - self.discount, 0) / self.bigram_counts[bi]

        # Case 3: backoff to bigram
        if self.bigram_counts[(w3, w4)] > 0:
            return max(self.bigram_counts[(w3, w4)] - self.discount, 0) / self.unigram_counts[uni]

        # Case 4: backoff to unigram
        return self.unigram_counts[w4] / self.total_unigrams if self.total_unigrams > 0 else 1e-6


def process_quadgram_file(input_file, output_file, discount=0.75):
    """
    Process the entire quadrigram file and save Katz Backoff probabilities to CSV.
    """
    model = KatzBackoffQuadgram(input_file, discount)

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        writer = csv.writer(outfile)
        writer.writerow(["w1", "w2", "w3", "w4", "count", "katz_backoff_prob"])

        for line in infile:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            w1, w2, w3, w4, count = parts
            prob_value = model.prob(w1, w2, w3, w4)
            writer.writerow([w1, w2, w3, w4, count, f"{prob_value:.8f}"])


if __name__ == "__main__":
    # Adjust file paths as needed
    input_path = "quadrigram_model.txt"
    output_path = "quadgram_katz_output.csv"

    process_quadgram_file(input_path, output_path, discount=0.75)
    print(f"Processing complete. Results saved to {output_path}")