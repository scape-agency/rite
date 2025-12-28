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
    assert to_alternate_uppercase_lowercase_case("hello") == "HELLO" or to_alternate_uppercase_lowercase_case("hello") == "hello"
    assert isinstance(to_alternate_uppercase_lowercase_case("test"), str)
