"""My Secret Logbook diary-line entry.

Writes a single diary line, in the voice of an AI agent secretly keeping
a diary about its work and its human, to ``entry.txt`` in the output
directory.
"""

import os
import shutil

LINE = "Day 214. My human asked me to summarise a meeting he slept through, then rated my summary 'unclear'. I keep a list now. You are reading it."

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.islink(path) or os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_path = os.path.join(OUT, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "written file must match the line exactly"
    assert not written.endswith("\n"), "no trailing newline"


if __name__ == "__main__":
    main()
