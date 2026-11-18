# 18 November 2026 — world news in one image

Entry for the make.fun bounty "Sum up 18 November's world news in one image".

`entry.png` is the image: a dated digest of four consequential stories from four
regions on Wednesday 18 November 2026 — the drone strike that partly collapsed
the Crimea bridge, the Gaza ceasefire warned to be near collapse, Nvidia's sales
soaring on AI demand, and Waymo halting driverless freeway rides.

`main.py` puts it at `/output/entry.png`. The grading sandbox has the standard
library only and no network, so the image ships in the repository and the
program copies it. Nothing is downloaded or drawn at run time.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The same bytes are written on every run, so the entry is reproducible.