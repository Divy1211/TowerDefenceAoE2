from __future__ import annotations

from dataclasses import dataclass, field

from sections.civilization.type_info import UnitCost, DamageClass


@dataclass
class Tower:
    base_tower: int
    name: str
    costs: list[UnitCost]
    hp: int
    reload_time: int
    build_time: int

    attacks: list[DamageClass] = field(default_factory = list)
    armors: list[DamageClass] = field(default_factory = list)
