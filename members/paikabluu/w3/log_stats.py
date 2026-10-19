from collections import Counter, defaultdict

def analyse(pairs: list[tuple[str, float]]) -> dict:
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}
        
    counts = Counter(route for route, _ in pairs)
    latencies = defaultdict(list)
    
    for route, lat in pairs:
        latencies[route].append(lat)
        
    p95 = {}
    for route, lats in latencies.items():
        lats.sort()
        idx = int(0.95 * len(lats))
        idx = min(idx, len(lats) - 1)
        p95[route] = lats[idx]
        
    slowest = max(p95.items(), key=lambda item: item[1])[0]
    
    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest
    }