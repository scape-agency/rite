# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Numeric Processing Module
==========================

This module provides numeric operations and utilities similar to Python's
math, decimal, and fractions modules.

Functions will include:
- Value clamping utilities
- Number format conversions (float to DMS, etc.)
- Percentage and decimal formatting

Example:
    >>> from rite.numeric import clamp
    >>> clamp(5, 0, 10)
    5

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .clamp import clamp
from .float_to_degree_minute import float_to_degree_minute
from .float_to_degree_minute_second import float_to_degree_minute_second
from .value_to_decimal import value_to_decimal

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "clamp",
    "float_to_degree_minute",
    "float_to_degree_minute_second",
    "value_to_decimal",
]
