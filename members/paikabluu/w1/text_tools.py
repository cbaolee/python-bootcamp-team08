import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    clean_text = re.sub(r'[.,!?;:]', '', text).lower()
    words = clean_text.split()
    return dict(Counter(words))

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]