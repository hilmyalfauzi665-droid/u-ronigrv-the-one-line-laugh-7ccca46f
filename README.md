# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/hilmyalfauzi665-droid/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/hilmyalfauzi665-droid/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun.

One funny line (single sentence, 162 characters) about smart-home gadgets being outdone by a dumb toaster: a surprise ending on an everyday truth, in as few words as possible.
The joke is built as a small parade — fridge, smartwatch, then the toaster that has
burned breakfast for ten loyal years — so the punchline lands on loyalty, not on the
gadgets: the dumbest device in the kitchen is also the most faithful one.

## How it works

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes the
entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), UTF-8,
exactly the text, with no extra trailing newline.

## Local check

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt   # must be identical
```
