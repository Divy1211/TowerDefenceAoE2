from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sections.civilization.type_info import UnitCost, DamageClass


@dataclass
class Tower:
    base_tower: int
    copy: bool = False

    upgrade_tech: int = None
    requires_tech: list[int] = None

    name: str = None
    costs: list[UnitCost] = None
    hp: int = None
    reload_time: int = None
    build_time: int = None

    attacks: list[DamageClass] = None
    armors: list[DamageClass] = None

    assigned_id: int = -1
