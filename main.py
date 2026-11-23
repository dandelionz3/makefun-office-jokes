import os

# Deterministic: no input, no randomness, no network — the same line every run.
LINE = "I got promoted to Senior, which turns out to mean the same meetings, except now I'm expected to have opinions in them."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
