#!/usr/bin/env python3
"""
Generate examples/examples.md by iterating over all .jpg files in the examples/ directory.
For each image, it creates a Markdown section with:
- Title derived from the filename (underscores → spaces, Title Case)
- The image displayed via Markdown syntax
- The description from the corresponding .txt file
- The Stable Diffusion prompt/settings from the corresponding .txt.sd.txt file
"""

import pathlib
import sys

def title_from_filename(stem: str) -> str:
    """Convert filename stem to Title Case with spaces."""
    return stem.replace('_', ' ').title()

def main():
    examples_dir = pathlib.Path(__file__).parent
    output_path = examples_dir / "examples.md"
    lines = []

    # Sort files for deterministic output
    for img_path in sorted(examples_dir.glob("*.jpg")):
        stem = img_path.stem  # e.g., "art_test"
        title = title_from_filename(stem)

        desc_path = examples_dir / f"{stem}.txt"
        prompt_path = examples_dir / f"{stem}.txt.sd.txt"

        # Verify required companion files exist
        if not desc_path.is_file():
            print(f"Warning: Description file missing for {img_path.name}, skipping.", file=sys.stderr)
            continue
        if not prompt_path.is_file():
            print(f"Warning: Prompt file missing for {img_path.name}, skipping.", file=sys.stderr)
            continue

        # Section header
        lines.append(f"## {title}\n")
        # Image
        lines.append(f"![{title}]({img_path.as_posix()})\n")
        lines.append("\n")
        # Description
        desc_text = desc_path.read_text(encoding="utf-8").strip()
        lines.append(f"{desc_text}\n\n")
        # Prompt header
        lines.append("**Stable Diffusion Prompt**\n\n")
        # Prompt content
        prompt_text = prompt_path.read_text(encoding="utf-8").strip()
        lines.append(f"{prompt_text}\n\n")
        # Optional separator for readability
        lines.append("---\n\n")

    # Write the collected markdown to examples.md
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
