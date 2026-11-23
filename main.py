import os

# One Word, First Thought: exactly one word, nothing else.
# Pick: "defenestration" — throwing something out a window. Against a
# field of soft, pretty rare words it wins on a sharp, vivid image plus
# wit: one concrete action you can picture instantly, not another
# lovely-sounding abstraction.
WORD = "defenestration"


def main():
    # Gate: exactly one word, 1-24 UTF-8 chars, no whitespace.
    assert WORD and len(WORD.encode("utf-8")) <= 24 and not any(c.isspace() for c in WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
