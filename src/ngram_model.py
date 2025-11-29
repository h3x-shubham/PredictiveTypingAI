import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from collections import defaultdict, Counter
from src.tokenize import load_cleaned_text, tokenize


from pathlib import Path
from collections import defaultdict, Counter
from src.tokenize import load_cleaned_text, tokenize


def build_trigram_counts(words: list[str]):
    trigram_counts = defaultdict(Counter)
    for i in range(len(words) - 2):
        w1, w2, w3 = words[i], words[i + 1], words[i + 2]
        trigram_counts[(w1, w2)][w3] += 1
    return trigram_counts

def predict_next_word(trigram_counts, w1: str, w2: str, top_k: int = 5):
    key = (w1.lower(), w2.lower())
    if key not in trigram_counts:
        return []
    counter = trigram_counts[key]
    return [word for word, count in counter.most_common(top_k)]
def main():
    print("Loading cleaned text...")
    cleaned = load_cleaned_text()

    print("Tokenizing...")
    words = tokenize(cleaned)
    print(f"Total words: {len(words)}")

    print("Building trigram model...")
    trigram_counts = build_trigram_counts(words)
    print(f"Unique (w1, w2) pairs: {len(trigram_counts)}")

    # Test predictions
    test_pairs = [
        ("mr", "holmes"),
        ("it", "was"),
        ("in", "the"),
        ("i", "am"),
    ]
    test_pairs = [
    ("sherlock", "holmes"),
    ("mr", "sherlock"),
    ("it", "was"),
    ("in", "the"),
    ("i", "am"),
    ]


    for w1, w2 in test_pairs:
        print(f"\nContext: {w1} {w2}")
        print("Suggestions:", predict_next_word(trigram_counts, w1, w2))


if __name__ == "__main__":
    main()