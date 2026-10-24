from __future__ import annotations

def route(task: str, providers: list[str]) -> list[str]:
    """Return provider ids for a parallel fan-out. Configurable, no redesign needed."""
    return list(providers)
