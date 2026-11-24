"""One-Sentence Absurd Invention Pitch -- make.fun entry.

The Umbrella for Your Phone: a tiny umbrella that follows your phone
everywhere, so it never has to face the rain, the sun, or the decision to
scroll in the shower. The entry is one sentence of at most 220 characters.
The program validates it, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "The Umbrella for Your Phone: a tiny umbrella that follows your phone "
    "everywhere so it never has to face the rain, the sun, or your decision "
    "to scroll in the shower."
)

MAX_LENGTH = 220
DESTINATION = "/output/entry.txt"


def validate(text):
    """Require one non-blank line of at most 220 characters, one sentence."""
    if not isinstance(text, str):
        raise ValueError("pitch must be text")
    if text != text.strip() or not text:
        raise ValueError("pitch must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("pitch is %d characters, over the 220 limit" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return text


def emit(text):
    """Print the pitch and write it to /output/entry.txt."""
    print(text)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")


def main():
    # Validate first, so only a well-formed pitch ever reaches the file.
    emit(validate(TEXT))


if __name__ == "__main__":
    main()
