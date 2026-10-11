from statistics import mean, median

def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list cannot be empty.")
    return {
        "min" : min(scores),
        "max" : max(scores),
        "mean" : round(mean(scores), 2),
        "median" : round(median(scores), 2)
    }
