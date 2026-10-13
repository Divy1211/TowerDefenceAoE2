from __future__ import annotations

from dataclasses import dataclass, field

from sections.civilization.type_info import UnitCost, DamageClass


@dataclass
class GameUnit:
    base_unit: int
    name: str
    costs: list[UnitCost]
    hp: int

    attacks: list[DamageClass] = field(default_factory = list)
    armors: list[DamageClass] = field(default_factory = list)
