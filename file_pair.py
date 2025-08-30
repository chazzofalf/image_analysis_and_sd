"""Module defining a simple container class for a pair of file paths.

The class enforces that exactly two items are provided during construction and
exposes them via read‑only properties ``description_file`` and
``stable_diffusion_file``.  No other attributes are intended to be accessed
from outside the class.
"""

from __future__ import annotations


class FilePair:
    """Container for a description file and a stable‑diffusion file.

    Parameters
    ----------
    files : list | tuple
        A sequence with exactly two items:
        * ``files[0]`` – path to the description file.
        * ``files[1]`` – path to the stable‑diffusion file.

    Raises
    ------
    ValueError
        If ``files`` is not a sequence of length two.
    """

    def __init__(self, files: list | tuple) -> None:
        if not isinstance(files, (list, tuple)):
            raise TypeError(
                "FilePair constructor expects a list or tuple of two items."
            )
        if len(files) != 2:
            raise ValueError(
                "FilePair requires exactly two items: "
                "[description_file, stable_diffusion_file]."
            )
        self._description_file = files[0]
        self._stable_diffusion_file = files[1]

    @property
    def description_file(self) -> str:
        """Read‑only path to the description file."""
        return self._description_file

    @property
    def stable_diffusion_file(self) -> str:
        """Read‑only path to the stable‑diffusion file."""
        return self._stable_diffusion_file

    # Prevent accidental addition of public attributes
    __slots__ = ("_description_file", "_stable_diffusion_file")


__all__ = ["FilePair"]
