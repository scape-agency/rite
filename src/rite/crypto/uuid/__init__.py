# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Identity Module
===============

This module provides unique identifier generation similar to
Python's uuid module.

Functions will include:
- UUID generation and utilities

Example:
    >>> from rite.identity import generate_uuid
    >>> generate_uuid()
    'a1b2c3d4-e5f6-...'

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .is_valid_uuid import is_valid_uuid

# Import | Local
from .uuid_hex import uuid_hex
from .uuid_random import uuid_random
from .uuid_string import uuid_string

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "uuid_hex",
    "uuid_random",
    "uuid_string",
    "is_valid_uuid",
]
