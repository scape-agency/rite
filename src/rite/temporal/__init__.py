# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Temporal Processing Module
===========================

This module provides time and date operations similar to Python's
datetime and time modules.

Functions will include:
- Timestamp operations
- Duration calculations
- Timezone utilities

Example:
    >>> from rite.temporal import timestamp
    >>> timestamp()
    1234567890.123

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .duration import Duration

# Import | Local
from .timestamp import Timestamp
from .timezone import Timezone

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "Timestamp",
    "Duration",
    "Timezone",
]
