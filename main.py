#!/usr/bin/env python3
"""Rename the Planet — make.fun bounty entry.

Writes the one-line entry text to /output/entry.txt (no trailing newline)
and prints it to stdout. Deterministic: the entry is a fixed constant,
so every run produces byte-identical output.
"""

from pathlib import Path

ENTRY = "Mars is now 'Refund.' Because after four billion years of red dust and no returns, it owes us all our money back."

# Bounty gates: entry must be 1-200 characters and a single line.
MIN_LENGTH = 1
MAX_LENGTH = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Validate the entry against the bounty gates before writing anything.
    assert MIN_LENGTH <= len(ENTRY) <= MAX_LENGTH, (
        f"entry length {len(ENTRY)} out of range "
        f"{MIN_LENGTH}-{MAX_LENGTH}"
    )
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
