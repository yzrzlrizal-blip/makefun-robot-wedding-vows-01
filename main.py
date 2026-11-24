"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow is fixed and deterministic: the same line
every run, so the entry is reproducible and the gate (1-160 UTF-8
characters, not only whitespace) always passes.
"""

from pathlib import Path

VOW = (
    "I promise to love you in sickness and in health, through every "
    "firmware update and low-battery warning, until death or a factory "
    "reset do us part."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate refuses any text outside 1-160 characters, so refuse
    # to write an over-long vow rather than submit an invalid entry.
    if not 1 <= len(VOW) <= 160 or not VOW.strip():
        raise ValueError(f"vow is {len(VOW)} characters; gate allows 1-160")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(VOW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
