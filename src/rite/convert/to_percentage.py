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


_percent_pat = re.compile(r"^\s*(?P<num>[-+]?\d*\.?\d+)\s*%?\s*$")


def to_percentage(x: Any) -> Optional[float]:
    """
    Accepts 35, "35", "35%", 0.35 (interpreted as 35 if 0<=x<=1), returns 0..100 float.
    """
    if x is None:
        return None
    if isinstance(x, (int, float)):
        val = float(x)
        if 0 <= val <= 1.0:
            val = val * 100.0
        return max(0.0, min(100.0, val))
    m = _percent_pat.match(str(x))
    if not m:
        return None
    val = float(m.group("num"))
    # If someone passes 0..1 as string, treat as fraction
    if 0 <= val <= 1.0:
        val = val * 100.0
    return max(0.0, min(100.0, val))


# =============================================================================
# Module Exports
# =============================================================================

__all__: List[str] = [
    "to_percentage",
]
