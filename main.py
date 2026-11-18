"""Write the entry image for the 18 November 2026 world-news bounty.

The graded sandbox has the standard library only and no network, so the image
ships in this repository beside this program and the program's whole job is to
put it at /output/entry.png. That is the simplest entry the rules describe.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png is missing beside this program")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(TARGET, os.path.getsize(TARGET), "bytes")


if __name__ == "__main__":
    main()