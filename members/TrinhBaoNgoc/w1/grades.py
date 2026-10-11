def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list must not empty!")
    sorted_scores = sorted(scores)
    length = len(scores)
    mid = length // 2
    median = 0
    if length % 2 == 0:
        median = (sorted_scores[mid] + sorted_scores[mid-1]) / 2
    else:
        median = sorted_scores[mid]
    return {
        "min" : sorted_scores[0],
        "max" : sorted_scores[length-1],
        "mean" : round(sum(scores) / length, 2),
        "median" : round(median, 2)
    }


