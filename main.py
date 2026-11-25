"""Write one original office joke to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), creates it, and writes
exactly one line plus a trailing newline. Standard library only.
"""

import os

JOKE = "The office printer only jams on urgent documents, so IT moved it to the org chart under 'emotional support animals'."

MAX_CHARS = 170


def main():
    line = JOKE.strip()
    if not line:
        raise ValueError("joke line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("joke line exceeds 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must not contain a newline")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Verify what landed on disk: exactly one line, trailing newline only.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("entry.txt does not contain exactly the joke line")


if __name__ == "__main__":
    main()
