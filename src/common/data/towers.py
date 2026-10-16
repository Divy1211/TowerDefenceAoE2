from prelude import *

from src.common.types import Tower
from src.common.data.techs import GUARD_TOWER, KEEP, INCENDIARIES, CHEMISTRY, BOMBARD_TOWER

WATCH_TOWER = Tower(base_tower = BuildingInfo.WATCH_TOWER.ID)
GUARD_TOWER = Tower(base_tower = BuildingInfo.GUARD_TOWER.ID, upgrade_tech = GUARD_TOWER)
KEEP = Tower(base_tower = BuildingInfo.KEEP.ID, upgrade_tech = KEEP)

FIRE_TOWER = Tower(base_tower = BuildingInfo.FIRE_TOWER.ID, requires_tech = [INCENDIARIES])

BOMBARD_TOWER = Tower(base_tower = BuildingInfo.BOMBARD_TOWER.ID, requires_tech = [CHEMISTRY, BOMBARD_TOWER])

basic_tower_line = [
    WATCH_TOWER,
    GUARD_TOWER,
    KEEP,
]

splash_tower_line = [
    FIRE_TOWER,
]

bombard_tower_line = [
    BOMBARD_TOWER,
]

ALL_TOWER_LINES = [
    basic_tower_line,
    splash_tower_line,
    bombard_tower_line,
]
