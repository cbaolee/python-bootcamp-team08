# text_tools.py

def word_count(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(str.maketrans("", "", ".,!?;:"))
    counts: dict[str, int] = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]
