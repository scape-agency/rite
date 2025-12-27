# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Conversion Module
=================

This module provides type conversion utilities similar to Python's
codecs and base64 modules.

Functions include:
- Boolean conversions
- Number conversions
- Decimal conversions
- Percentage conversions
- Bytes conversions
- Protected type checking

Example:
    >>> from rite.conversion import to_bool, to_bytes
    >>> to_bool("yes")
    True
    >>> to_bytes("hello")
    b'hello'

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .is_protected_type import PROTECTED_TYPES, is_protected_type

# Import | Local
from .to_bool import to_bool
from .to_bytes import to_bytes
from .to_number import to_number
from .to_percentage import to_percentage

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "to_bool",
    "to_number",
    "to_percentage",
    "to_bytes",
    "is_protected_type",
    "PROTECTED_TYPES",
]
