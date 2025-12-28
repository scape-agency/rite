# =============================================================================
# Test: case_to_pig_latin
# =============================================================================

"""
Tests for rite.text.case.case_to_pig_latin.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_pig_latin import (
    to_pig_latin_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_pig_latin_case() -> None:
    """Test to_pig_latin_case() function."""
    result = to_pig_latin_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_to_pig_latin_case_consonant_start() -> None:
    """Test pig latin for words starting with consonant."""
    assert to_pig_latin_case("hello") == "ellohay"
    assert to_pig_latin_case("pig") == "igpay"
    assert to_pig_latin_case("latin") == "atinlay"


def test_to_pig_latin_case_vowel_start() -> None:
    """Test pig latin for words starting with vowel."""
    assert to_pig_latin_case("apple") == "appleway"
    assert to_pig_latin_case("orange") == "orangeway"
    assert to_pig_latin_case("under") == "underway"


def test_to_pig_latin_case_multiple_words() -> None:
    """Test pig latin for multiple words."""
    assert to_pig_latin_case("hello world") == "ellohay orldway"
    assert to_pig_latin_case("i love you") == "iway ovelay ouyay"
