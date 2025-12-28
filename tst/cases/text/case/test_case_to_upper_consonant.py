# =============================================================================
# Test: case_to_upper_consonant
# =============================================================================

"""
Tests for rite.text.case.case_to_upper_consonant.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_upper_consonant import (
    to_consonant_uppercase_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_consonant_uppercase_case() -> None:
    """Test to_consonant_uppercase_case() function."""
    assert to_consonant_uppercase_case("hello") == "HELLO" or to_consonant_uppercase_case("hello") == "hello"
    assert isinstance(to_consonant_uppercase_case("test"), str)
