# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Remove None Utility
===================

This module provides a utility function to filter None values from dictionaries.

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


def dict_remove_none(d: dict[str, Any]) -> dict[str, Any]:
    """
    Return a new dict omitting all keys with None values.

    Args:
        d: Dictionary to filter.

    Returns:
        New dictionary with None values removed.
    """
    return {k: v for k, v in d.items() if v is not None}


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "dict_remove_none",
]
