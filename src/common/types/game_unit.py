from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sections.civilization.type_info import UnitCost, DamageClass


@dataclass
class GameUnit:
    base_unit: int
    copy: bool = True

    name: str = None
    costs: list[UnitCost] = None
    hp: int = None
    location: int = None
    button: int = None

    attacks: list[DamageClass] = None
    armors: list[DamageClass] = None

    assigned_id: int = -1
