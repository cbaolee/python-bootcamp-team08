def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list cannot be empty.")
    s = sorted(scores)
    n = len(s)
    mid = n // 2
    med = (s[mid] + s[mid-1]) / 2 if n % 2 == 0 else s[mid]
    
    return {
        "min" : min(scores),
        "max" : max(scores),
        "mean" : round(sum(scores) / n, 2),
        "median" : round(med, 2)
    }
