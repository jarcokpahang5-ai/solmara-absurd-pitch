"""One-Sentence Absurd Invention Pitch -- make.fun entry.

One sentence, at most 220 characters, pitching an absurd invention: a tiny
umbrella that follows your phone everywhere. The program validates the
sentence, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

PITCH = (
    "The Umbrella for Your Phone: a tiny umbrella that follows your phone "
    "everywhere so it never has to face the rain, the sun, or your decision "
    "to scroll in the shower."
)

LIMIT = 220
OUTPUT_PATH = "/output/entry.txt"


def check_pitch(text):
    """One sentence, 1 to 220 characters, not blank, a single line."""
    if not isinstance(text, str):
        raise ValueError("pitch must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if len(text) > LIMIT:
        raise ValueError("pitch is %d characters, over the 220 limit" % len(text))
    if text.count(".") > 1:
        raise ValueError("pitch must be one sentence")
    return text


def main():
    pitch = check_pitch(PITCH)
    print(pitch)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(pitch + "\n")


if __name__ == "__main__":
    main()
