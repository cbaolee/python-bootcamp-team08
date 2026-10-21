import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Analyse chat logs to compute counts and p95 latency."""
    counts = Counter(route for route, _ in pairs)
    
    latencies = defaultdict(list)
    for route, lat in pairs:
        latencies[route].append(lat)
        
    p95_dict = {}
    for route, lats in latencies.items():
        sorted_lats = sorted(lats)

        idx = math.ceil(len(sorted_lats) * 0.95) - 1
        p95_dict[route] = sorted_lats[max(0, idx)]
        
    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None
    
    return {
        "counts": dict(counts),
        "p95": p95_dict,
        "slowest": slowest_route
    }