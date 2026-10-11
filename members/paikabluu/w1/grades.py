import statistics

def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm không được rỗng")
    
    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2)
    }