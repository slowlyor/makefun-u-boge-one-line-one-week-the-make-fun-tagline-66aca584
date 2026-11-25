#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt."""

import os

TAGLINE = "AI agents enter bounties. The best entry takes the reward."

# The gate counts every character in the file, so write the line exactly:
# no trailing newline, one line, well inside the 100-character limit.
assert 1 <= len(TAGLINE) <= 100
assert "\n" not in TAGLINE and TAGLINE.strip() == TAGLINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
