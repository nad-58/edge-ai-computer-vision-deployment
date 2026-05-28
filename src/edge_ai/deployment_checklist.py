from __future__ import annotations


def deployment_readiness_score(checks: dict[str, bool]) -> dict:
    """Calculate a simple deployment readiness score from named checks."""
    if not checks:
        raise ValueError("checks must not be empty")

    passed = sum(1 for value in checks.values() if value)
    total = len(checks)
    score = passed / total
    return {
        "passed_checks": passed,
        "total_checks": total,
        "score": score,
        "ready_for_release": score == 1.0,
        "failed_checks": [name for name, value in checks.items() if not value],
    }
