"""Statistics for chat-log (route, latency_ms) pairs."""

import math
from collections import Counter, defaultdict


def _p95(values: list[float]) -> float:
    """Nearest-rank 95th percentile."""
    ordered = sorted(values)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Return request counts, p95 latency per route and the slowest route."""
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)
    p95 = {route: _p95(values) for route, values in latencies.items()}
    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
