from pathlib import Path

from prelude import *

from datfile.build import create_dat
from scx.build import create_scx

def main():
    out_mod_path = Path(Paths.MODS_LOCAL_DIR) / "PvPTowerDefence"
    create_dat(out_mod_path)
    create_scx(out_mod_path)

if __name__ == "__main__":
    main()
