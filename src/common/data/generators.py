from prelude import *

from src.common.types import Generator, GenRate

GOLD_GENERATOR = Generator(base_building = BuildingInfo.MINING_CAMP.ID, generates = [GenRate(ResourceId.GOLD_STORAGE, 1.0)])
STONE_GENERATOR = Generator(base_building = BuildingInfo.MINING_CAMP.ID, generates = [GenRate(ResourceId.STONE_STORAGE, 1.0)])
WOOD_GENERATOR = Generator(base_building = BuildingInfo.LUMBER_CAMP.ID, generates = [GenRate(ResourceId.WOOD_STORAGE, 1.0)])
FOOD_GENERATOR = Generator(base_building = BuildingInfo.MILL.ID, generates = [GenRate(ResourceId.FOOD_STORAGE, 1.0)])

ALL_GENERATORS = [
    GOLD_GENERATOR,
    STONE_GENERATOR,
    WOOD_GENERATOR,
    FOOD_GENERATOR,
]
