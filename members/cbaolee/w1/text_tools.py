def word_count(text: str) -> dict[str, int]:
    """Count the appearances of each word in a string, a word is defined by a continuos sub-string without space and punctuation"""
    temp_text: str = text.lower()

    for punctuation in ".,!?;:":
        temp_text = temp_text.replace(punctuation, "")

    words: list[str] = temp_text.split()

    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k words based on their appearances"""
    counts: dict[str, int] = word_count(text)

    sorted_words: list[tuple[str, int]] = sorted(counts.items(), key=lambda x: (-x[1],x[0]))

    return sorted_words[:k]