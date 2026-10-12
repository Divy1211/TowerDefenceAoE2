## Welcome :)

## Dev Setup

Setup:
  - `uv` is required to work with this project. Follow the steps [here](https://docs.astral.sh/uv/getting-started/installation/) to install `uv` if you do not have it already
  - Clone with `git clone --recurse-submodules https://github.com/Divy1211/TowerDefenceAoE2.git`
  - `cd` into the cloned folder and run `uv sync`
  - Change the steam ID in `prelude.common_vars.py` to your own.
  - Run with `uv run python -m src.main`
  - Optionally: You may want to symlink the `src/xs` folder to your profile folder's `xs/TowerDefence`
    - On windows, this can be done using `mklink /D link_dir target_dir`