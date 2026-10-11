import statistics


# return a dict include: min, max, mean, median values.
# Raise ValueError when the input list is empty.
def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("scores empty")
    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }
