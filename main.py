#!/usr/bin/env python3
"""One Mango, Perfectly Ripe — make.fun entry.

Writes one picture of a single ingredient (a perfectly ripe mango)
to <output>/entry.png. Standard library only, no network, deterministic:
every run copies the same bundled image bytes, so two runs produce
byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSET = HERE / "dish.png"


def main() -> int:
    # Output dir from the environment so the sandbox can point it anywhere;
    # default is the bounty-standard /output.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    with ASSET.open("rb") as src, dest.open("wb") as out:
        shutil.copyfileobj(src, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
