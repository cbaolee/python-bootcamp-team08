import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float]]) -> dict:
    counts = Counter()
    latencies_by_route = defaultdict(list)
    
    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)
        
    p95_latencies = {}
    
    for route, latencies in latencies_by_route.items():
        sorted_lats = sorted(latencies)
        
        idx = math.ceil(len(sorted_lats) * 0.95) - 1
        idx = max(0, min(idx, len(sorted_lats) - 1))
        
        p95_latencies[route] = sorted_lats[idx]
        
    slowest_route = max(p95_latencies, key=p95_latencies.get) if p95_latencies else None
    
    return {
        "counts": counts,
        "p95": p95_latencies,
        "slowest": slowest_route
    }