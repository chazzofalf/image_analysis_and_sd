"""output_file_pair.py

Provides a convenience wrapper class that, given a single input image filename,
generates the corresponding description and stable‑diffusion markdown file
paths using :func:`generate_output_paths` and then exposes those paths via
the same read‑only properties as :class:`FilePair`.

The wrapper class is deliberately lightweight: it stores an internal
:class:`FilePair` instance and forwards the two public properties.
"""

from __future__ import annotations

from output_path_generator import generate_output_paths
from file_pair import FilePair


class OutputFilePair:
    """Convenient wrapper around :class:`FilePair`.

    Parameters
    ----------
    input_filename : str
        The image filename (relative or absolute) for which output markdown
        files should be generated.

    The constructor uses :func:`generate_output_paths` to obtain the two
    output filenames and creates an internal :class:`FilePair` instance.
    The wrapper then re‑exposes the read‑only ``description_file`` and
    ``stable_diffusion_file`` properties directly.
    """

    def __init__(self, input_filename: str) -> None:
        # Generate the two output markdown paths
        output_paths = generate_output_paths(input_filename)

        # Initialise the underlying FilePair with the generated paths
        self._pair = FilePair(output_paths)

    @property
    def description_file(self) -> str:
        """Read‑only path to the description markdown file."""
        return self._pair.description_file

    @property
    def stable_diffusion_file(self) -> str:
        """Read‑only path to the stable‑diffusion markdown file."""
        return self._pair.stable_diffusion_file

    # Prevent accidental addition of public attributes
    __slots__ = ("_pair",)


__all__ = ["OutputFilePair"]
