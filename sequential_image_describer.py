"""
sequential_image_describer.py

Utility script that sequentially runs the `main` function from `image_describer.py`
for each supplied image file.

The core entry point is the `process_images` function, which can be used
programmatically or via the command‑line interface.

Usage (CLI):
    python sequential_image_describer.py <image1> <image2> ...

Programmatic usage:
    from sequential_image_describer import process_images
    process_images('img1.jpg', 'img2.png')
"""

import sys
from typing import Iterable
from image_describer import main as image_describer_main


def _process_single(image_path: str) -> None:
    """
    Invoke the `image_describer.main` function for a single image.
    Any exception raised by the underlying script is caught and reported
    so that processing can continue with the next image.
    """
    try:
        image_describer_main(image_path)
    except Exception as e:  # pragma: no cover
        print(f"[ERROR] Failed to process {image_path}: {e}")


def process_images(*image_paths: str) -> None:
    """
    Sequentially process one or more image files using the logic defined in
    `image_describer.main`.

    Parameters
    ----------
    *image_paths : str
        One or more filenames (paths) to be processed. At least one argument
        must be provided.

    Raises
    ------
    ValueError
        If no image paths are supplied.
    """
    if not image_paths:
        raise ValueError("At least one image path must be provided to process_images().")

    for path in image_paths:
        _process_single(path)


if __name__ == "__main__":
    # Simple command‑line wrapper: forward all arguments (except the script name)
    # to `process_images`.
    if len(sys.argv) < 2:
        print("Usage: python sequential_image_describer.py <image_path1> [<image_path2> ...]")
        sys.exit(1)

    process_images(*sys.argv[1:])
