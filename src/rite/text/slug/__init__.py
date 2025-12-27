# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Slug Generation Module
=======================

Functions for generating URL-friendly slugs.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .add_slug_prefix import add_slug_prefix
from .add_slug_suffix import add_slug_suffix
from .is_valid_slug import is_valid_slug

# Import | Local Modules
from .slugify import slugify
from .unique_slug import unique_slug

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "slugify",
    "add_slug_prefix",
    "add_slug_suffix",
    "unique_slug",
    "is_valid_slug",
]
