#!/usr/bin/env python3
"""news-image-20261120 v5 entrypoint.

Copies the pre-rendered front page (entry.png) to the output directory
the harness provides. Byte-identical on every run: no rendering happens
here, the image is a fixed asset.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
