# =============================================================================
# Docstring
# =============================================================================

"""
CSV Delimiter Detection
=======================

Provides functionality to detect the delimiter used in a CSV file based on its
filename extension.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Functions
# =============================================================================


def detect_delimiter(filename: str) -> str:
    """
    Detect the delimiter used in a CSV file based on its filename.

    Args:
    ----
        filename: The name or path of the CSV file.

    Returns:
    -------
        str: The detected delimiter character (tab or comma).

    """
    if filename.endswith(".tsv"):
        return "\t"
    return ","


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "detect_delimiter",
]
