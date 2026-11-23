import os

# Deterministic: no input, no randomness, no network — the same line every run.
LINE = "I got promoted to Senior, which turns out to mean the same meetings, except now I'm expected to have opinions in them."

# The gate requires 1-199 characters: fail loudly instead of writing an invalid entry.
assert 1 <= len(LINE) <= 199, f"entry must be 1-199 chars, got {len(LINE)}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
