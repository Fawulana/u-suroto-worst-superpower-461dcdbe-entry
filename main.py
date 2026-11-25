"""Worst Superpower entry.

Writes a single line inventing the most useless superpower imaginable
to /output/entry.txt. Deterministic, offline, stdlib only: the exact
same bytes are written on every run.
"""

import os

LINE = (
    "I can sense the exact second any microwave finishes cooking "
    "\u2014 but only other people's, and only once the beeping has "
    "already stopped."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate validation: 1-140 characters, single line, not whitespace-only.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-140")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must not span multiple lines")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: write the line exactly as-is.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify the round-trip: what landed on disk must be exactly LINE.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("output file does not match the entry line")


if __name__ == "__main__":
    main()
