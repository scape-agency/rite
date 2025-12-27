# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Diagnostics Module
==================

This module provides error handling and logging utilities similar to
Python's logging, warnings, and traceback modules.

Functions will include:
- Logging utilities
- Error handlers
- Exception utilities

Example:
    >>> from rite.diagnostics import logger
    >>> logger.info("Application started")

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .error_handler import ErrorHandler

# Import | Local
from .logger import Logger

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "Logger",
    "ErrorHandler",
]
