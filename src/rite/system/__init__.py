

# =============================================================================
# Docstring
# =============================================================================

"""
System Module
=============

This module provides system-level operations similar to Python's
subprocess, sys, and os modules.

Functions will include:
- Command execution
- I/O operations

Example:
    >>> from rite.system import run_command
    >>> run_command("ls -la")

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local
from .run_command import run_command

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "run_command",
]
