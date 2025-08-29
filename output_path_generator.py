"""output_path_generator.py

Utility module to generate output markdown file paths based on an input image file.
"""

from pathlib import Path
from typing import List


def generate_output_paths(input_path: str) -> List[str]:
    """
    Given a path to an image file, return a list containing two markdown file paths:
    1. <stem>_Description.md
    2. <stem>_Stable_Diffusion.md

    The returned paths preserve the input path style:
    * If a relative path is provided, the returned paths are relative.
    * If an absolute path is provided, the returned paths are absolute.

    Parameters
    ----------
    input_path : str
        Path to the source image. Can be absolute, relative, or ``./`` prefixed.

    Returns
    -------
    List[str]
        List with two path strings matching the input style.
    """
    # Resolve the input path, preserving relative vs absolute
    img_path = Path(input_path).expanduser()
    if img_path.is_absolute():
        img_path = img_path.resolve()

    # Extract the stem (filename without suffix) and parent directory
    stem = img_path.stem
    parent = img_path.parent

    # Build the two output filenames
    description_path = parent / f"{stem}_Description.md"
    sd_path = parent / f"{stem}_Stable_Diffusion.md"

    # Return path strings matching the input style
    return [str(description_path), str(sd_path)]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate markdown output paths for an image file."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        default="Scout.jpg",
        help="Path to the input image file (relative or absolute).",
    )
    args = parser.parse_args()

    outputs = generate_output_paths(args.input_path)
    print("Generated output paths:")
    for p in outputs:
        print(p)
