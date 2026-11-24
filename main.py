"""Comedy status report, one line.

Writes one line (<=200 chars) to /output/entry.txt.
"""

import os


def main():
    line = (
        "Weekly status: everything is green, on track, and operational "
        "— except the product, which has been down since Tuesday, but "
        "nobody reads past the first line anyway."
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote /output/entry.txt ({len(line)} characters)")


if __name__ == "__main__":
    main()
