# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Markup Module
=============

This module provides markup language handling similar to Python's
html and xml modules.

Functions will include:
- HTML cleaning and manipulation

Example:
    >>> from rite.markup import clean_html
    >>> clean_html("<p>Hello</p>")
    'Hello'

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .clean_html import clean_html

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "clean_html",
]
