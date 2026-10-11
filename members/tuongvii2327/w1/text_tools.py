# return a dict includes: word : number of time exist.
def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.split()
    counts = {}
    for word in text:
        counts[word] = counts.get(word, 0) + 1
    return counts


# return a tuple after reversed str with int
def sort_key(item: tuple[str, int]) -> tuple[int, str]:
    return (-item[1], item[0])


# return k words with the most number of time existed in str
# (if more than k words, sort by alphabetically)
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    count = word_count(text)
    items = count.items()
    ordered = sorted(items, key=sort_key)
    return ordered[:k]
