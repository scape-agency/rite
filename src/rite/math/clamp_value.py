# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Starling PolyPlan -
==========================================


"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import re
from typing import Any, List, Optional

# Import | Libraries


# Import | Local Modules

# =============================================================================
# Functions
# =============================================================================


def clamp(
    val: Optional[float],
    lo: float,
    hi: float,
) -> Optional[float]:
    """
    Clamp a value between a lower and upper bound.
    """

    if val is None:
        return None

    return max(lo, min(hi, val))


# =============================================================================
# Module Exports
# =============================================================================

__all__: List[str] = [
    "clamp",
]
