#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic, Python 3.13 standard library only.

The line (83 characters, one sentence, no trailing newline):

    The glass was see-through, so it was already a ghost, and I don't live with ghosts.
"""

import os
import sys

ENTRY = "The glass was see-through, so it was already a ghost, and I don't live with ghosts."


def validate(data: bytes) -> str:
    """Check the exact gate invariants on the bytes to be written.

    Returns the decoded line, or raises ValueError naming the failure.
    """
    text = data.decode("utf-8")  # raises on invalid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if data.endswith(b"\n"):
        raise ValueError("entry must have no trailing newline")
    return text


def main() -> int:
    data = ENTRY.encode("utf-8")
    try:
        text = validate(data)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    # Read back and confirm the file holds exactly the validated bytes.
    with open(path, "rb") as fh:
        if fh.read() != data:
            print("entry.txt does not match the validated bytes", file=sys.stderr)
            return 1
    print(f"entry.txt: {len(text)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
