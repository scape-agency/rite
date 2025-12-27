# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Filename to Date String Module
==============================

Extracts date strings from filenames using pattern matching.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import Optional

# Import | Local Modules
from rite.time.date_format_to_regex import date_format_to_regex

# =============================================================================
# Functions
# =============================================================================


def filename_to_datestring(
    filename: str,
    date_format: str = "%Y-%m-%d-%H%M%S",
) -> Optional[str]:
    """
    Extract the date string from a filename using the given format.

    Args:
    ----
        filename: Filename to search for date pattern.
        date_format: strftime format string to match against.

    Returns:
    -------
        Date string if found, otherwise None.

    """
    regex = date_format_to_regex(date_format)
    search = regex.search(filename)
    if search:
        return search.groups()[0]
    return None


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "filename_to_datestring",
]
