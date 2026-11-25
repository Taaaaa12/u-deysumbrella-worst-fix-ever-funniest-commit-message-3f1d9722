#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line (at most 100 characters) for a bug
fix that made everything worse, to /output/entry.txt.
"""

import os

ENTRY = "fix: stop the crash by removing the button users kept pressing"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 100, "entry must be 1-100 characters"
    assert text == text.splitlines()[0], "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
