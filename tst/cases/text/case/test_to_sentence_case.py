# =============================================================================
# Test: to_sentence_case
# =============================================================================

"""
Tests for rite.text.case.to_sentence_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.text.case.to_sentence_case import (
    to_sentence_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_sentence_case() -> None:
    """Test to_sentence_case() function."""
    result = to_sentence_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_to_sentence_case_lowercase() -> None:
    """Test to_sentence_case with lowercase input."""
    assert to_sentence_case("hello world") == "Hello world"


def test_to_sentence_case_uppercase() -> None:
    """Test to_sentence_case with uppercase input."""
    assert to_sentence_case("HELLO WORLD") == "Hello world"


def test_to_sentence_case_mixed() -> None:
    """Test to_sentence_case with mixed case."""
    assert to_sentence_case("hElLo WoRlD") == "Hello world"


def test_to_sentence_case_empty() -> None:
    """Test to_sentence_case with empty string."""
    assert to_sentence_case("") == ""


def test_to_sentence_case_single_char() -> None:
    """Test to_sentence_case with single character."""
    assert to_sentence_case("a") == "A"
    assert to_sentence_case("A") == "A"
