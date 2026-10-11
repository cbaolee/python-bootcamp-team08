def word_count(text : str) -> dict[str, int]: 
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, " ")
    count = {}
    for word in text.lower().split():
        count[word] = count.get(word, 0) + 1
    
    return count 

def top_k(text : str, k : int) -> list[tuple[str, int]]:
    counts = word_count(text)
    ranked = sorted(counts.items(), key = lambda item: (-item[1], item[0]))
    return ranked[:max(k, 0)]