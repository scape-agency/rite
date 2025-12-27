# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
File Size to String Converter Module
====================================

Provides functionality to convert file sizes to human-readable strings.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import BinaryIO, Protocol, Union

# Import | Local Modules
# Implement local bytes-to-string conversion to avoid external dependency.

SIZE_UNITS: tuple[str, ...] = (
    "B",
    "KB",
    "MB",
    "GB",
    "TB",
    "PB",
)


def _convert_bytes_to_string(value: int) -> str:
    if value < 0:
        return "0 B"
    idx = 0
    size = float(value)
    while size >= 1024 and idx < len(SIZE_UNITS) - 1:
        size /= 1024
        idx += 1
    if idx == 0:
        return f"{int(size)} {SIZE_UNITS[idx]}"
    return f"{size:.2f} {SIZE_UNITS[idx]}"


# =============================================================================
# Classes
# =============================================================================


class _SizedStream(Protocol):
    """Protocol for file-like objects with a size attribute."""

    size: int

    def tell(self, *args, **kwargs) -> int: ...
    def seek(self, *args, **kwargs) -> int: ...


# =============================================================================
# Functions
# =============================================================================


def file_size_to_string(
    filehandle: Union[BinaryIO, _SizedStream],
) -> str:
    """Return the size of a file in a human-readable string.

    Attempts to use filehandle.size if available (e.g. Django's UploadedFile),
    otherwise seeks to the end to determine size.

    Args:
    ----
        filehandle: A file-like object.

    Returns:
    -------
        str: A string representing the file size, e.g., '2.4 MB', '1 KB'.

    """
    if hasattr(filehandle, "size"):
        try:
            return _convert_bytes_to_string(int(filehandle.size))
        except (AttributeError, TypeError, ValueError):  # pragma: no cover
            pass

    try:
        current_position = filehandle.tell()
        filehandle.seek(0, 2)  # Move to end
        size = filehandle.tell()
        filehandle.seek(current_position)  # Reset to original position
        return _convert_bytes_to_string(int(size))
    except (AttributeError, OSError, TypeError, ValueError):
        return "Unknown size"


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "file_size_to_string",
]
