from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING

from prelude import *
from sections.civilization.type_info import UnitClass, UnitCost
from sections.civilization import Unit as Object
from src.common.data import ALL_TOWER_LINES
from src.common.utils import clone

if TYPE_CHECKING:
    from sections.datfile_sections import DatFile
    from src.common.types import Tower


def set_stats(tower: Object, tower_info: Tower):
    pass


def add_towers(dat: DatFile, xs: XsWriter):
    tower_names = []

    for civ_id, civ in enumerate(dat.civilizations):
        locations = iter(GameInfo.BUTTON_LOCATIONS)
        hotkey_ids = iter(GameInfo.HOTKEY_ID_MAP.values())
        for tower_info in chain(*ALL_TOWER_LINES): # type: Tower
            tower = civ.units[tower_info.base_tower]
            assert tower is not None, f"Base tower {tower_info.base_tower} is None"

            set_stats(tower, tower_info)

            tower_wall = clone(tower)

            tower_wall.id = len(civ.units)
            tower_wall.base_id = len(civ.units)
            tower_wall.copy_id = len(civ.units)
            tower_info.assigned_id = len(civ.units)

            if civ_id == 0:
                name = to_pascal(tower_info.name)
                xs(f"extern const int c{name} = {tower.id};")
                xs(f"extern const int c{name}Wall = {tower_wall.id};")
                xs()
                tower_names.append(name)

            tower_wall.class_ = UnitClass.Wall
            tower_wall.enabled = True
            tower_wall.creation_info.train_locations[0].train_time = 10
            tower_wall.creation_info.train_locations[0].location_unit_id = UnitInfo.VILLAGER_MALE_BUILDER.ID
            tower_wall.creation_info.train_locations[0].button_id = next(locations)
            tower_wall.creation_info.train_locations[0].hotkey_id = next(hotkey_ids)

            tower_wall.building_info.adjacent_mode = civ.units[
                BuildingInfo.PALISADE_WALL.ID].building_info.adjacent_mode
            tower_wall.building_info.disappears_when_built = True
            tower_wall.building_info.stack_unit_id = tower.id

            tower_wall.creation_info.costs = [
                UnitCost(),
                UnitCost(),
                UnitCost(),
            ]

            civ.units.append(tower_wall)

    with xs.fn("int", "mapWallToTower", ["int id = -1"]):
        with xs.switch("id"):
            for name in tower_names:
                with xs.case_(f"c{name}Wall"):
                    xs(f"return (c{name});")
        xs('xsChatData("Error: Missing Wall to Tower ID");')
        xs('return (-1);')
