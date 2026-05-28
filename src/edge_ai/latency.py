from __future__ import annotations

from statistics import mean
from typing import Sequence


def latency_summary(latency_ms: Sequence[float]) -> dict:
    """Summarise model inference latency measurements in milliseconds."""
    if not latency_ms:
        raise ValueError("latency_ms must contain at least one measurement")

    sorted_values = sorted(float(value) for value in latency_ms)
    p50_index = int(0.50 * (len(sorted_values) - 1))
    p95_index = int(0.95 * (len(sorted_values) - 1))

    return {
        "count": len(sorted_values),
        "mean_ms": mean(sorted_values),
        "min_ms": sorted_values[0],
        "max_ms": sorted_values[-1],
        "p50_ms": sorted_values[p50_index],
        "p95_ms": sorted_values[p95_index],
    }


def latency_acceptance(summary: dict, target_ms: float) -> dict:
    """Assess latency against a target using p95 latency."""
    p95_ms = float(summary["p95_ms"])
    return {
        "target_ms": target_ms,
        "p95_ms": p95_ms,
        "passed": p95_ms <= target_ms,
        "margin_ms": target_ms - p95_ms,
    }
