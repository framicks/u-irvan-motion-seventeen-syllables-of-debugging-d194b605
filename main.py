"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging to entry.txt.
Stdlib only, no network, deterministic: the same bytes every run.
"""

import os
from pathlib import Path

HAIKU = (
    "One last print statement\n"
    "left in the code at midnight\n"
    "ships to production\n"
)

# Syllable count, word by word (17 total, 5-7-5):
#   Line 1 (5): One(1) last(1) print(1) state-ment(2)
#   Line 2 (7): left(1) in(1) the(1) code(1) at(1) mid-night(2)
#   Line 3 (5): ships(1) to(1) pro-duc-tion(3)
# The picture is concrete — a leftover debug print at midnight — and the
# last line turns it: the throwaway line ships to production.


def main() -> None:
    lines = HAIKU.strip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert len(HAIKU) <= 200, f"haiku is {len(HAIKU)} chars, over the 200 limit"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(HAIKU, encoding="utf-8")
    print(f"Wrote {len(HAIKU)} characters to {target}")


if __name__ == "__main__":
    main()
