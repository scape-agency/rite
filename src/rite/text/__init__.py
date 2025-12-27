# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Text Processing Module
======================

This module provides text processing utilities similar to Python's str,
string, and textwrap modules.

The text module includes functions for:
- Case conversions (snake_case, camelCase, PascalCase, kebab-case, etc.)
- Slug generation for URL-friendly strings
- Text analysis (character frequency, word count, etc.)
- String sanitization and cleaning
- Morse code encoding/decoding
- Random string generation

Example:
    >>> from rite.text import to_snake_case, slugify
    >>> to_snake_case("Hello World")
    'hello_world'
    >>> slugify("Hello World!")
    'hello-world'

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from .analysis import char_frequency, is_palindrome, longest_word, word_count

# Import | Local Modules
from .case import (
    to_camel_case,
    to_constant_case,
    to_dot_case,
    to_kebab_case,
    to_lower_case,
    to_pascal_case,
    to_path_case,
    to_sentence_case,
    to_snake_case,
    to_title_case,
    to_upper_case,
)
from .morse import morse_decode, morse_encode
from .random import random_alphanumeric, random_hex, random_string
from .sanitize import clean, sanitize
from .slug import add_slug_prefix, add_slug_suffix, slugify, unique_slug

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    # Case conversions
    "to_snake_case",
    "to_camel_case",
    "to_pascal_case",
    "to_kebab_case",
    "to_constant_case",
    "to_dot_case",
    "to_path_case",
    "to_title_case",
    "to_sentence_case",
    "to_lower_case",
    "to_upper_case",
    # Slug generation
    "slugify",
    "add_slug_prefix",
    "add_slug_suffix",
    "unique_slug",
    # Analysis
    "char_frequency",
    "word_count",
    "is_palindrome",
    "longest_word",
    # Sanitization
    "sanitize",
    "clean",
    # Morse code
    "morse_encode",
    "morse_decode",
    # Random generation
    "random_string",
    "random_hex",
    "random_alphanumeric",
]
