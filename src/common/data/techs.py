from prelude import *

from src.common.types import GameTech

CHEMISTRY = GameTech(base_tech = TechInfo.CHEMISTRY.ID)
INCENDIARIES = GameTech(base_tech = TechInfo.INCENDIARIES.ID)

BOMBARD_TOWER = GameTech(base_tech = TechInfo.BOMBARD_TOWER.ID)
GUARD_TOWER = GameTech(base_tech = TechInfo.GUARD_TOWER.ID)
KEEP = GameTech(base_tech = TechInfo.KEEP.ID)

ALL_TECHS = [
    CHEMISTRY,
    INCENDIARIES,
    BOMBARD_TOWER,

    GUARD_TOWER,
    KEEP,
]
