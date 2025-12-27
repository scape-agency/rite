# =============================================================================
# Test: is_palindrome
# =============================================================================

"""
Tests for rite.text.analysis.is_palindrome.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.analysis.is_palindrome import (
    is_palindrome,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_is_palindrome() -> None:
    """Test is_palindrome() function."""
    # Test basic palindromes
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True

    # Test non-palindromes
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False

    # Test empty string
    assert is_palindrome("") is True

    # Test with case sensitivity
    assert is_palindrome("Racecar", ignore_case=True) is True
    assert is_palindrome("Racecar", ignore_case=False) is False
