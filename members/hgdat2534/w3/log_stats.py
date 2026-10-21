"""Route latency analysis and percentile aggregation utilities."""

import math
from collections import Counter, defaultdict
from collections.abc import Sequence
from typing import Any


def analyse(pairs: Sequence[tuple[str, float]]) -> dict[str, Any]:
    """Compute request counts, p95 latency per route, and the slowest route.

    Args:
        pairs: A sequence of (route, latency_ms) tuples.

    Returns:
        A dictionary with keys 'counts', 'p95', and 'slowest'.
    """
    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)

    p95_latencies: dict[str, float] = {}

    for route, latencies in latencies_by_route.items():
        sorted_lats = sorted(latencies)
        idx = math.ceil(len(sorted_lats) * 0.95) - 1
        idx = max(0, min(idx, len(sorted_lats) - 1))
        p95_latencies[route] = sorted_lats[idx]

    slowest_route: str | None = (
        max(p95_latencies, key=lambda r: p95_latencies[r])
        if p95_latencies
        else None
    )

    return {
        "counts": counts,
        "p95": p95_latencies,
        "slowest": slowest_route,
    }