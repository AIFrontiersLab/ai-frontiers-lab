from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Settings:
    concept_id: int = 34
    concept_name: str = 'Hybrid Search Engine'
    max_candidates: int = 20
    require_evidence: bool = True
    stages: list[str] = field(default_factory=lambda: [])
