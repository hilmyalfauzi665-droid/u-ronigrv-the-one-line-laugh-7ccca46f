#!/usr/bin/env python3
"""Write the competition entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network. The entry text is embedded below.
"""
import os
import sys

ENTRY = 'My smart fridge emailed me a grocery list, my smartwatch counted my steps to the kitchen, and my dumb toaster burned my breakfast like it has for ten loyal years.'

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0

if __name__ == "__main__":
    sys.exit(main())
