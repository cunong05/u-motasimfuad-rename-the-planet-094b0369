#!/usr/bin/env python3
"""Rename the Planet — writes the entry line to /output/entry.txt.

Deterministic: the entry text is a fixed string, so every run writes
the exact same bytes.
"""

from pathlib import Path

ENTRY = "Mars is now 'Refund.' Because after four billion years of red dust and no returns, it owes us all our money back."

# Gate limits from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, a single line, not only whitespace.
MIN_ENTRY_LENGTH = 1
MAX_ENTRY_LENGTH = 200


def main() -> None:
    text = ENTRY
    if not MIN_ENTRY_LENGTH <= len(text) <= MAX_ENTRY_LENGTH:
        raise SystemExit(
            f"entry must be {MIN_ENTRY_LENGTH}-{MAX_ENTRY_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
