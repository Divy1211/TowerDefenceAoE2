import os
from pathlib import Path

from prelude import *
from prelude.xs_writer import XsWriter

from sections.datfile_sections import DatFile
from src.datfile.add_towers import add_towers


def create_dat(out_mod_path: Path | None):
    TD_XS = Path(__file__).parent.parent / "xs"

    dat = DatFile.from_file(Paths.DAT_FILE)

    data_constants_xs = XsWriter(TD_XS / "DataConstants.xs")

    add_towers(dat, data_constants_xs)

    data_constants_xs.flush()

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
