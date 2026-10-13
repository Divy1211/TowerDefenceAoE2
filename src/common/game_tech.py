from __future__ import annotations

from dataclasses import dataclass, field

from sections.tech import TechCost
from src.common.game_tech_effect import GameTechEffect


@dataclass
class GameTech:
    base_tech: int
    name: str
    location: int
    button: int
    costs: list[TechCost]

    override_effects: list[GameTechEffect] | None = None
    extra_effects: list[GameTechEffect] = field(default_factory = list)

    min_required_count: int = 1
    required_techs: list[int] = field(default_factory = list)
