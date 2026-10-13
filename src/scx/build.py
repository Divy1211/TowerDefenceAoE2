import os
from pathlib import Path

from prelude import *

from src.scx.map import MAP_SIZE, define_areas
from src.scx.player_setup import player_setup


def create_scx(out_mod_path: Path | None):
    in_name = "Parser Bases/Base 2p.aoe2scenario"
    scx = AoE2DEScenario.from_default()
    out_name = "PvPTowerDefence.aoe2scenario"

    tm = scx.trigger_manager
    mm = scx.map_manager
    um = scx.unit_manager
    xsm = scx.xs_manager

    verstr = add_credits_header(f"TD", "0.1.0", scx)
    out_name = f"{out_name.removesuffix('.aoe2scenario')} v{verstr}.aoe2scenario"

    xsm.script_name = r"TowerDefence\TowerDefence"

    mm.map_size = MAP_SIZE

    um.units[PlayerId.GAIA].clear()

    player_setup(scx)
    define_areas(scx)

    um.add_unit(PlayerId.ONE, UnitInfo.VILLAGER_MALE.ID, 4, 4)

    if out_mod_path is not None:
        out_scx_dir = out_mod_path / "resources" / "_common" / "scenario"
        out_scx_dir.mkdir(exist_ok = True, parents = True)
        for file in os.listdir(out_scx_dir):
            if file.startswith(out_name[:20]):
                os.unlink(out_scx_dir / file)
        scx.write_to_file(str(out_scx_dir / out_name))
    else:
        xsm.script_name = r"TowerDefenceDev\TowerDefence"
        for file in os.listdir(Paths.SCENARIO_DIR):
            if file.startswith("!dev_" + out_name[:20]):
                os.unlink(Paths.SCENARIO_DIR + file)
        scx.write_to_file(Paths.SCENARIO_DIR + "!dev_" + out_name)

if __name__ == '__main__':
    create_scx(None)
