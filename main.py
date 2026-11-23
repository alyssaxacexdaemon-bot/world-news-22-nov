#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261122 bounty.

Copies the entry image (entry.png, shipped in this repository) to the
output directory as entry.png. Standard library only: nothing is
installed before this program runs, and it makes no network calls.
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ENTRY_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, ENTRY_NAME)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        print("error: copied entry.png has the wrong size", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
