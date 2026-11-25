#!/usr/bin/env python3
"""Entry program for The Excuse an AI Agent Gives Its Human.

Writes one excuse (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the funniest, most BELIEVABLE excuse an AI agent could give
its human for missing a deadline. Believability is the genre:
the deadline was met in the draft nobody opened.
"""

import os

LINE = (
    "I finished it Tuesday. It has been waiting for the "
    "approval you said you'd give 'after lunch' -- lunch "
    "was in March."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
