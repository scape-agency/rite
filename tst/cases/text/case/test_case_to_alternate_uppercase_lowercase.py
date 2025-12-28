# =============================================================================
# Test: case_to_alternate_uppercase_lowercase
# =============================================================================

"""
Tests for rite.text.case.case_to_alternate_uppercase_lowercase.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_alternate_uppercase_lowercase import (
    to_alternate_uppercase_lowercase_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_alternate_uppercase_lowercase_case() -> None:
    """Test to_alternate_uppercase_lowercase_case() function."""
    result = to_alternate_uppercase_lowercase_case("hello")
    assert result == "hElLo"
    assert isinstance(result, str)
    # Verify alternating pattern: even indices lowercase, odd indices uppercase
    for i, char in enumerate(result):
        if i % 2 == 0:
            assert char.islower() or not char.isalpha()
        else:
            assert char.isupper() or not char.isalpha()
