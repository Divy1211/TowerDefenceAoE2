from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sections.tech import TechCost
    from src.common.types.game_tech_effect import GameTechEffect


@dataclass
class GameTech:
    base_tech: int
    copy: bool = False

    name: str = None
    location: int = None
    button: int = None
    costs: list[TechCost] = None

    effects: list[GameTechEffect] = None
    extra_effects: list[GameTechEffect] = field(default_factory = list)

    min_required_count: int = -1
    required_techs: list[GameTech] = field(default_factory = list)

    assigned_id: int = -1
