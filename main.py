#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (<= 320 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only.
"""

import os
import re

ENTRY = (
    "The senator who just wrote 900 pages of AI regulation still emails "
    "his intern a Word file named FINAL_final_v7_REAL.docx asking her to "
    "turn it into a PDF, then wonders why the future keeps sending him "
    "to voicemail."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars, must be 1-320"
    # One sentence: exactly one sentence terminator (a . ! or ? followed by
    # whitespace or end of text). Dots inside filenames (e.g. .docx) don't count.
    assert len(re.findall(r"[.!?](?:\s|$)", text)) == 1, "entry must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
