from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sections.civilization.type_info import UnitCost

@dataclass
class GenRate:
    resource: int
    rate_per_second: float

@dataclass
class Generator:
    base_building: int
    generates: list[GenRate]
    copy: bool = True

    name: str = None
    costs: list[UnitCost] = None
    hp: int = None
    location: int = None
    button: int = None
    required_terrain: int = -1

    assigned_id: int = -1
