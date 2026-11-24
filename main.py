#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes a single pickup line (1-200 characters) to the grader's output
path. Python 3, standard library only.
"""

import os
import sys

ENTRY = "Insert exact change, press B4, and I'll drop the sweetest thing in this whole machine \u2014 fair warning, it's me."


def output_path():
    """Resolve the grader's output path."""
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    text = ENTRY
    # Gate: the entry must be 1..200 characters of non-whitespace text.
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry length %d outside 1..200" % len(text))
    if not text.strip():
        raise SystemExit("entry is blank")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
