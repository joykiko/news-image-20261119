"""Entry for make.fun news-image-20261119: sum up 19 November 2026 in one image.

The front page ships in this repository as entry.png. The program writes
that exact image, byte for byte, to the output directory make.fun gives it.
It uses no network and writes the same bytes on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Copy the shipped front page to the grader's output directory."""
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(OUT, "entry.png"),
    )


if __name__ == "__main__":
    main()
