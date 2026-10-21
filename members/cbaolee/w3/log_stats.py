from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """The statics of route list with its latency"""
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}
    
    routes = [route for route, latency in pairs]
    counts = Counter(routes)

    latency_map = defaultdict(list)
    for route, latency in pairs:
        latency_map[route].append(latency)

    p95_dict = {}
    for route, latencies in latency_map.items():
        sorted_lats = sorted(latencies)
        idx = int(0.95 * len(sorted_lats))
        if idx >= len(sorted_lats):
            idx = len(sorted_lats) - 1
            
        p95_dict[route] = float(sorted_lats[idx])

    slowest_route = max(p95_dict, key=p95_dict.get)

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route
    }