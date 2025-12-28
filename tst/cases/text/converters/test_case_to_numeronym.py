# =============================================================================
# Test: case_to_numeronym
# =============================================================================

"""
Tests for rite.text.converters.case_to_numeronym.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_numeronym import (
    to_numeronym_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_numeronym_case() -> None:
    """Test to_numeronym_case() function."""
    result = to_numeronym_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_to_numeronym_case_basic() -> None:
    """Test basic numeronym conversion."""
    assert to_numeronym_case("Internationalization") == "I18n"
    assert to_numeronym_case("localization") == "l10n"
    assert to_numeronym_case("accessibility") == "a11y"


def test_to_numeronym_case_short_words() -> None:
    """Test words with 3 or fewer characters return unchanged (line 41)."""
    assert to_numeronym_case("a") == "a"
    assert to_numeronym_case("ab") == "ab"
    assert to_numeronym_case("abc") == "abc"
    assert to_numeronym_case("abcd") == "a2d"


def test_to_numeronym_case_edge_cases() -> None:
    """Test edge cases."""
    assert to_numeronym_case("") == ""
    assert to_numeronym_case("test") == "t2t"
