import os
import shutil
from pathlib import Path

from bfp_rs import BaseStruct

from prelude import *
from prelude.xs_writer import XsWriter

from sections.civilization.type_info.creation_info import TrainLocation
from sections.datfile_sections import DatFile
from sections.civilization.type_info import UnitClass, UnitCost

from src.common.tower_data import TOWER_DATA


def clone[T: BaseStruct](struct: T) -> T:
    return struct.from_bytes(struct.to_bytes(), ver = struct.ver, strict = True)

def create_dat(out_mod_path: Path | None):
    TD_XS = Path(__file__).parent.parent / "xs"

    dat = DatFile.from_file(Paths.DAT_FILE)

    xs = XsWriter(TD_XS / "DataConstants.xs")
    tower_names = []

    for civ_id, civ in enumerate(dat.civilizations):
        locations = iter(range(1, 16))
        hotkey_ids = iter([
            16135, # Q
            16128, # W
            16171, # E
            16169, # R
            16144, # T

            16099, # A
            16068, # S
            16085, # D
            16093, # F
            16156, # G

            16089, # Z
            16186, # X
            16142, # C
            16445, # V
            16179, # B
        ])
        for building in TOWER_DATA:
            tower = civ.units[building.ID]
            if tower is None:
                continue

            tower.combat_info.attacks = []
            tower.combat_info.armors = []

            tower_wall = clone(tower)

            tower_wall.id = len(civ.units)
            tower_wall.base_id = len(civ.units)
            tower_wall.copy_id = len(civ.units)

            if civ_id == 0:
                name = to_pascal(building.name)
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

            tower_wall.building_info.adjacent_mode = civ.units[BuildingInfo.PALISADE_WALL.ID].building_info.adjacent_mode
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
    xs.flush()

    if out_mod_path is not None:
        dat_folder = out_mod_path / "resources" / "_common" / "dat"
        dat_folder.mkdir(parents = True, exist_ok = True)
        dat.to_file(str(dat_folder / "empires2_x2_p1.dat"))

        DatFile.from_file(str(dat_folder / "empires2_x2_p1.dat"))

        OUT_XS_DIR = out_mod_path / "resources" / "_common" / "xs" / "TowerDefence"
        OUT_XS_DIR.mkdir(parents = True, exist_ok = True)
        for file in os.listdir(TD_XS):
            with open(TD_XS / file) as infile, open(OUT_XS_DIR / file, "w") as outfile:
                outfile.write(
                    infile.read()
                        .replace("TowerDefenceDev", "TowerDefence")
                        .replace("include \"TowerDefenceDev\\Effects.xs\";", "include \"TowerDefenceDev\\Constants.xs\";")
                )

if __name__ == '__main__':
    create_dat(None)
