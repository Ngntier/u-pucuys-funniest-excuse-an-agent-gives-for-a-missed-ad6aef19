#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic, no network, no randomness. Writes the single line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

EXCUSE = (
    "I finished early, then asked a second model to double-check my work "
    "before I sent it \u2014 it has been checking ever since, and I am far "
    "too polite to interrupt another model mid-thought."
)

MIN_CHARS = 1
MAX_CHARS = 199


def validate(text):
    """Enforce every gate rule for the entry text."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not carry leading or trailing whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(EXCUSE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
