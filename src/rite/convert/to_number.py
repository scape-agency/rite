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


_number_pat = re.compile(r"^\s*([-+]?\d*\.?\d+)\s*(?:[a-zA-Z%/]*?)\s*$")


def to_number(x: Any) -> Optional[float]:
    """
    Parse a number from messy strings like '20 m', '45.5 %', '100/ha'.
    """
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    m = _number_pat.match(str(x))
    return float(m.group(1)) if m else None


# =============================================================================
# Module Exports
# =============================================================================

__all__: List[str] = [
    "to_number",
]
