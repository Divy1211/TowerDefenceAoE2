from __future__ import annotations

from dataclasses import dataclass, field

from sections.civilization.type_info import UnitCost

@dataclass
class Rate:
    resource: int
    rate_per_second: float

@dataclass
class Generator:
    base_building: int
    name: str

    costs: list[UnitCost]

    generates: list[Rate]

    min_required_count: int = 1
    required_techs: list[int] = field(default_factory = list)
