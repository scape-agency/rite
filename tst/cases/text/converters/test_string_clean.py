# =============================================================================
# Test: string_clean
# =============================================================================

"""
Tests for rite.text.converters.string_clean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.string_clean import (
    string_clean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_string_clean() -> None:
    """Test string_clean() function."""
    result = string_clean("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_string_clean_whitespace() -> None:
    """Test string_clean strips whitespace."""
    assert string_clean("  hello  ") == "hello"
    assert string_clean("\t\nhello\n\t") == "hello"


def test_string_clean_none_input() -> None:
    """Test string_clean with None input."""
    assert string_clean(None) is None


def test_string_clean_empty_string() -> None:
    """Test string_clean with empty string returns None."""
    assert string_clean("") is None
    assert string_clean("   ") is None


def test_string_clean_none_string() -> None:
    """Test string_clean with 'none' string returns None."""
    assert string_clean("none") is None
    assert string_clean("None") is None
    assert string_clean("NONE") is None


def test_string_clean_null_string() -> None:
    """Test string_clean with 'null' string returns None."""
    assert string_clean("null") is None
    assert string_clean("Null") is None
    assert string_clean("NULL") is None
