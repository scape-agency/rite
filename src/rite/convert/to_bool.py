# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Rite - Utilities - Convert to Boolean
=====================================

This module provides a utility function for converting various types of
values to boolean.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import Any, List, Optional

# Import | Libraries


# Import | Local Modules

# =============================================================================
# Functions
# =============================================================================


TRUTHY = {"true", "t", "yes", "y", "1", "on"}
FALSY = {"false", "f", "no", "n", "0", "off", ""}


def to_bool(x: Any) -> Optional[bool]:
    """
    Convert a value to a boolean.
    """

    # Handle None
    if x is None:
        return None

    # Handle booleans
    if isinstance(x, bool):
        return x

    # Handle numbers
    if isinstance(x, (int, float)):
        return bool(int(x))

    # Handle strings
    s = str(x).strip().lower()
    if s in TRUTHY:
        return True
    if s in FALSY:
        return False

    # Let validators raise if required
    return None


# =============================================================================
# Exports
# =============================================================================

__all__: List[str] = [
    "to_bool",
]
