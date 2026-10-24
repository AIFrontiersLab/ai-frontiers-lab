from __future__ import annotations

def completed(stages: dict, name: str) -> bool:
    return (stages.get(name) or {}).get("status") == "completed"
