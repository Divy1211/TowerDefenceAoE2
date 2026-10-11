from pathlib import Path

from prelude import *

from src.scx.map import MAP_SIZE, define_areas
from src.scx.player_setup import player_setup


def create_scx(out_mod_path: Path | None):
    in_name = "Parser Bases/Base 2p.aoe2scenario"
    out_name = "PvPTowerDefence.aoe2scenario"
    scx = AoE2DEScenario.from_file(Paths.SCENARIO_DIR + in_name)
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

    if out_mod_path is not None:
        scx.write_to_file(str(out_mod_path / "resources" / "_common" / "scenario" / out_name))
    else:
        scx.write_to_file(Paths.SCENARIO_DIR + "!test_" + out_name)


if __name__ == '__main__':
    create_scx(None)
