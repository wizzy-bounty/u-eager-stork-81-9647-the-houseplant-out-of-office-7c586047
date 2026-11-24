#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- writes one houseplant OOO auto-reply.

Deterministic, stdlib only, no network. Writes the entry text to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

ENTRY = "Out of office: the fern, unwatered since March, has unionized with the dust and gone on strike. No replies until rain."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry length out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
