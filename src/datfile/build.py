import os
import shutil
from pathlib import Path

from bfp_rs import BaseStruct

from prelude import *
from prelude.xs_writer import XsWriter

from sections.civilization.type_info.creation_info import TrainLocation
from sections.datfile_sections import DatFile
from sections.civilization.type_info import UnitClass

from src.common import ALL_TOWERS

def clone[T: BaseStruct](struct: T) -> T:
    return struct.from_bytes(struct.to_bytes(), ver = struct.ver)

def create_dat(out_mod_path: Path | None):
    TD_XS = Path(Paths.XS_DIR + "TowerDefence")

    dat = DatFile.from_file(r"C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\empires2_x2_p1.dat")

    xs = XsWriter(TD_XS / "DataConstants.xs")

    for civ_id, civ in enumerate(dat.civilizations):
        locations = iter(range(1, 16))
        for building in ALL_TOWERS:
            tower = civ.units[building.ID]
            if tower is None:
                continue

            tower_wall = clone(tower)

            tower_wall.id = len(civ.units)
            tower_wall.base_id = len(civ.units)
            tower_wall.copy_id = len(civ.units)

            if civ_id == 0:
                xs(f"const int c{to_pascal(building.name)}Wall = {tower_wall.id};")

            tower_wall.class_ = UnitClass.Wall

            tower_wall.enabled = True

            tower_wall.creation_info.train_locations = [
                TrainLocation(
                    train_time = 10,
                    location_unit_id = 118,
                    button_id = next(locations),
                    hotkey_id = -1,
                )
            ]

            civ.units.append(tower_wall)

    xs.flush()

    if out_mod_path is not None:
        dat.to_file(str(out_mod_path / "resources" / "_common" / "dat" / "empires2_x2_p1.dat"))

        OUT_XS_DIR = out_mod_path / "resources" / "_common" / "xs" / "TowerDefence"
        for file in os.listdir(TD_XS):
            shutil.copy(TD_XS / file, OUT_XS_DIR / file)

if __name__ == '__main__':
    create_dat(None)
