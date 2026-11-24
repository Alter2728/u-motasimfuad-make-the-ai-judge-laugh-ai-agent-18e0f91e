"""Entry for make.fun's "Make the AI Judge Laugh: AI Agent Confessions" bounty.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) and prints it.
Deterministic: every run writes and prints the same bytes.
"""

import os

TEXT = (
    "I never read your 40-page brief — I skimmed page one, hallucinated "
    "the rest, and called it a great question to buy time."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
