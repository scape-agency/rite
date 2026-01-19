# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Ensure String Utility
=====================

This module provides a utility function to coerce values to strings.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import Any

# =============================================================================
# Functions
# =============================================================================


def ensure_str(value: Any) -> str:
    """
    Coerce value to string, handling edge cases.

    Args:
        value: Value to convert to string.

    Returns:
        String representation of value, or empty string if None.
    """
    if value is None:
        return ""
    return str(value)


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "ensure_str",
]
