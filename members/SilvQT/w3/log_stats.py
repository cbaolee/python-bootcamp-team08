from collections import Counter
from math import ceil


def analyse(pairs) -> dict:
    """
    Analyses request log pairs of (route, latency_ms).
    Returns request counts per route, p95 latency per route,
    route with highest p95 latency.
    """
    count = Counter(route for route, latency in pairs)
    latencies ={}

    for route, latency in pairs:
        if route not in latencies:
            latencies[route] = []

        latencies[route].append(latency)

    p95 = {}
    for route, values in latencies.items():
        values.sort()
        index = ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return{
        "counts": dict(count),
        "p95": p95,
        "slowest": slowest
    }
