from prelude import *

from sections.civilization.type_info import UnitCost

from src.common.tower import Tower

TOWER_DATA = [
    BuildingInfo.WATCH_TOWER,
    BuildingInfo.GUARD_TOWER,
    BuildingInfo.KEEP,
    BuildingInfo.BOMBARD_TOWER,
    BuildingInfo.FIRE_TOWER,
    BuildingInfo.SEA_TOWER,
]

# TOWER_DATA = {
#     BuildingInfo.WATCH_TOWER: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.WOOD_STORAGE, quantity = 35),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
#     BuildingInfo.GUARD_TOWER: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.WOOD_STORAGE, quantity = 35),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
#     BuildingInfo.KEEP: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.WOOD_STORAGE, quantity = 35),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
#
#     BuildingInfo.BOMBARD_TOWER: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.GOLD_STORAGE, quantity = 100),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
#     BuildingInfo.FIRE_TOWER: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.GOLD_STORAGE, quantity = 100),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
#
#     BuildingInfo.SEA_TOWER: Tower(
#         costs = [
#             UnitCost(resource_id = ResourceId.WOOD_STORAGE, quantity = 35),
#             UnitCost(resource_id = ResourceId.STONE_STORAGE, quantity = 125),
#         ],
#         build_time = 5
#     ),
# }
