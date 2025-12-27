

# =============================================================================
# Docstring
# =============================================================================

"""
Reflection Module
=================

This module provides runtime introspection utilities similar to
Python's importlib and inspect modules.

Functions will include:
- Dynamic class loading
- Module introspection

Example:
    >>> from rite.reflection import load_class
    >>> MyClass = load_class("mymodule.MyClass")

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .load_class import ClassImportError, load_class

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "load_class",
    "ClassImportError",
]
