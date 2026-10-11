def word_count(text: str) -> dict[str, int]:
    for char in [".", ",", "!", "?", ";", ":"]:
        text = text.replace(char, "")
    
    words = text.lower().split()
    counter = {}
    for i in words:
        counter[i] = counter.get(i, 0) + 1
    
    return counter

def top_k(text: str, k:int) -> list[tuple[str, int]]:
    counter = word_count(text)
    
    #Sort words by frequency, then alphabetically
    sorted_words = sorted(counter.items(), key=lambda item:(-item[1], item[0]))
    
    return sorted_words[:k]