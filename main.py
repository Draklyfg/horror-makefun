"""Write one two-sentence horror story to the output file."""

import os


STORY = "Every night, my son kisses me goodnight and whispers that he loves me. Tonight he whispered it in my dead father's voice, and he has never met my father."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
