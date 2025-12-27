

# =============================================================================
# Docstring
# =============================================================================

"""
Functional Programming Module
==============================

This module provides functional programming utilities similar to
Python's functools and operator modules.

Functions will include:
- Function decorators
- Debounce utilities
- Other functional programming patterns

Example:
    >>> from rite.functional import debounce
    >>> @debounce(0.5)
    ... def my_function():
    ...     pass

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .debounce import debounce

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "debounce",
]
