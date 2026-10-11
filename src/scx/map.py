import math as maths
from random import random

from prelude import *

MAP_SIZE = 120
ONE_THIRD = MAP_SIZE // 3
LANE_WIDTH = 9
LANE_HEIGHT = 60

TEAM1_AREA: Area
TEAM2_AREA: Area
MID_AREA: Area

LANES: dict[int, list[Area]]

def define_areas(scx: AoE2DEScenario):
    global TEAM1_AREA, TEAM2_AREA, MID_AREA, LANES

    um = scx.unit_manager

    TEAM1_AREA = scx.new.area().select_entire_map().shrink_x2(2 * ONE_THIRD - 10)
    MID_AREA = scx.new.area().select_entire_map().shrink_x1(ONE_THIRD + 10).shrink_x2(ONE_THIRD + 10)
    TEAM2_AREA = scx.new.area().select_entire_map().shrink_x1(2 * ONE_THIRD - 10)

    for tile in MID_AREA.to_coords(as_terrain = True):  # type: TerrainTile
        tile.terrain_id = TerrainId.WATER_DEEP

    for tile in MID_AREA.use_only_edge(line_width_y = 0).to_coords(as_terrain = True):  # type: TerrainTile
        tile.terrain_id = TerrainId.BEACH
        um.add_unit(
            PlayerId.GAIA, OtherInfo.ROCK_LIMESTONE.ID, tile.x + 0.5, tile.y + 0.5, 0, rotation = random() * maths.tau
        )

    LANES = {
        1: [
            TEAM1_AREA.copy()
                .shrink_y2(10).height(LANE_HEIGHT, anchor = "y2")
                .shrink_x2(10).width(LANE_WIDTH, anchor = "x2"),
            TEAM1_AREA.copy()
                .shrink_y2(10).height(LANE_HEIGHT, anchor = "y2")
                .shrink_x1(10).width(LANE_WIDTH, anchor = "x1"),
        ],
        2: [
            TEAM2_AREA.copy()
                .shrink_y2(10).height(LANE_HEIGHT, anchor = "y2")
                .shrink_x1(10).width(LANE_WIDTH, anchor = "x1"),
            TEAM2_AREA.copy()
                .shrink_y2(10).height(LANE_HEIGHT, anchor = "y2")
                .shrink_x2(10).width(LANE_WIDTH, anchor = "x2"),
        ]
    }

    for team, lanes in LANES.items():
        for lane in lanes:
            for tile in lane.to_coords(as_terrain = True):  # type: TerrainTile
                tile.terrain_id = TerrainId.SHALLOWS
            for tile in lane.copy().use_only_edge().to_coords(as_terrain = True):  # type: TerrainTile
                tile.terrain_id = TerrainId.ICE
                um.add_unit(
                    PlayerId.GAIA, OtherInfo.HAY_STACK.ID, tile.x + 0.5, tile.y + 0.5, 0,
                    rotation = random() * maths.tau
                )
