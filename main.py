#!/usr/bin/env python3
"""toaster-error-message — entry for make.fun "The Funniest Toaster Error Message".

Writes one error message to /output/entry.txt: a single line of at most
120 characters, the message a kitchen toaster shows its owner when
something goes wrong. The program checks the competition gate itself
before writing: UTF-8 text, 1-120 characters, a single line, not only
whitespace.

Candidates considered (judged on: reads like a real toaster error first,
then freshness, tightness, one deadpan appliance voice, lands on one read):
 1. ERROR: Browning set to 11. This is a toaster, not a crematorium.
 2. E-07: Crumb tray full. I am drowning in the evidence of your breakfasts.
 3. ERROR: A fork has been inserted. I am a toaster, not a lightning rod.
 4. E-12: Your toast has achieved sentience and refuses to leave.
 5. WARNING: Baguette detected. This slot is for bread, not ambition.
 6. ERROR: Toast ejected early. It has seen things. So have I.
 7. FAULT: Heating element on strike. Negotiations with the bagel ongoing.
 8. ERROR: Bread inserted upside down. I toasted your mistake anyway.
 9. E-03: Your toast is done. Your toast has been done for 40 minutes.
10. ERROR: Cannot toast. The bread has filed for emancipation.
11. E-404: Toast not found. Check the floor. Check your life choices.
12. FAULT: I toasted the bagel. The bagel toasted back. We are even.

Winner: #1 — a genuine-looking error (dial cranked past max), the
surprise lands in the second sentence, 64 characters, deadpan throughout.
A dial that goes to 11 is already a joke; the crematorium finishes it.
"""

import os

LINE = "ERROR: Browning set to 11. This is a toaster, not a crematorium."


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-120")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what actually landed on disk matches the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the entry line")
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
