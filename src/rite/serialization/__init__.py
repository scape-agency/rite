# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Serialization Module
====================

This module provides data serialization utilities similar to Python's
json, csv, and pickle modules.

Functions will include:
- JSON utilities (stdlib only)
- CSV utilities (stdlib only)
- INI/config file handling
- Object serialization

Example:
    >>> from rite.serialization import json_load
    >>> data = json_load("data.json")

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .csv_utils import detect_delimiter
from .ini_utils import INIHandler

# Import | Local
from .json_utils import JSONHandler

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "JSONHandler",
    "detect_delimiter",
    "INIHandler",
]
