def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("Score list cannot be empty.")
    
    sorted_scores = sorted(scores)
    score_len = len(sorted_scores)    
    min_val = min(scores)
    max_val = max(scores)
    mean_val = round(sum(scores) / score_len, 2)
    
    if score_len % 2 == 1:
        median_val = sorted_scores[score_len // 2]
    else:
        median_val = (sorted_scores[score_len//2 -1] + sorted_scores[score_len // 2]) / 2
    median_val = round(median_val, 2)
    return{
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val,
    }
    
    
    
    
    
    
    