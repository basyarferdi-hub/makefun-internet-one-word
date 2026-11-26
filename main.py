"""Entry for make.fun bounty: The Internet in One Word.

Writes one English word (1-30 characters, letters only, no spaces, no
punctuation) to entry.txt in the output directory.
Deterministic: every run writes exactly the same bytes.
No network access, no external files, no dependencies.
"""

import sys
from pathlib import Path

WORD = "Everything"


def output_dir() -> Path:
    """Use /output when it is available (grader), else a local output folder."""
    grader_dir = Path("/output")
    try:
        grader_dir.mkdir(parents=True, exist_ok=True)
        probe = grader_dir / ".write_probe"
        probe.write_text("", encoding="utf-8")
        probe.unlink()
        return grader_dir
    except OSError:
        local = Path("output")
        local.mkdir(parents=True, exist_ok=True)
        return local


def main() -> None:
    assert 1 <= len(WORD) <= 30, "word must be 1 to 30 characters"
    assert WORD.isalpha(), "word must contain letters only"
    if len(sys.argv) > 1:
        # Optional explicit target, used for local testing only.
        target = Path(sys.argv[1])
        target.parent.mkdir(parents=True, exist_ok=True)
    else:
        target = output_dir() / "entry.txt"
    target.write_text(WORD + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
