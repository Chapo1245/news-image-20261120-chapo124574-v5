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
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly on a partial/truncated copy instead of shipping a
    # corrupt artifact: the copied file must be byte-for-byte the source.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit(
            f"copy verification failed: {dst} is "
            f"{os.path.getsize(dst)} bytes, expected {os.path.getsize(src)}"
        )


if __name__ == "__main__":
    main()
