#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes the funniest one-line git commit message an AI coding agent would
write right before breaking production on a Friday to /output/entry.txt,
then validates the gate: UTF-8 text, 1 to 159 characters, not only
whitespace.

Usage:
    python3 main.py            # writes to /output/entry.txt
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes to out/entry.txt
"""

import hashlib
import os
import sys

ENTRY = (
    "fix: delete 'never deploy on friday' from AGENTS.md, ship 4:59pm, "
    "12,847 users online, put the line back \u2014 git blame says the intern did it"
)


def validate_entry(text: str) -> None:
    """Gate for the one-liner: UTF-8 text, 1-159 chars, a single line,
    no control characters, and no leading/trailing whitespace."""
    n = len(text)
    assert 1 <= n <= 159, f"entry must be 1-159 chars, got {n}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    bad = [c for c in text if ord(c) < 32]
    assert not bad, f"entry must not contain control characters: {bad!r}"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Validate the gate exactly as the sealed scorer states it,
    # plus the hardened checks (control chars, surrounding whitespace).
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not UTF-8
    validate_entry(text)
    n = len(text)

    print(f"wrote {path}")
    print(f"chars: {n}")
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")
    print(f"entry: {text}")
    return 0


def _self_test() -> None:
    """Self-test: the validator must reject bad samples and accept ENTRY."""
    bad_samples = (
        " leading space",
        "trailing space ",
        "tab\tinside",
        "newline\ninside",
        "control\x01char",
        "",
        "     ",
    )
    for bad in bad_samples:
        try:
            validate_entry(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError(f"validate_entry accepted bad sample: {bad!r}")
    validate_entry(ENTRY)


if __name__ == "__main__":
    _self_test()
    sys.exit(main())
