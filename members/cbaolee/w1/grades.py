def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Your list is empty!")

    n: int = len(scores)
    sum: float = 0
    
    temp_scores = scores
    temp_scores.sort()

    for score in scores:
        sum += score

    grades = {
        "min": temp_scores[0],
        "max": temp_scores[n - 1],
        "mean": round(sum / n, 2),
        "median": round(temp_scores[int((n - 1) / 2)] if (n % 2 != 0) else (temp_scores[int(n / 2) - 1] + temp_scores[int(n / 2)]) / 2, 2)
    }

    return grades