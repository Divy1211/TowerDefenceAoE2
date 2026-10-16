from prelude import *

from src.common.types import GameUnit

BUILDER = GameUnit(base_unit = UnitInfo.VILLAGER_MALE_BUILDER.ID, copy = False)
CAR = GameUnit(base_unit = UnitInfo.COBRA_CAR.ID)

ALL_UNITS = [
    BUILDER,
    CAR,
]
