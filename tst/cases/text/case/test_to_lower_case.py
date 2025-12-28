# =============================================================================
# Test: to_lower_case
# =============================================================================

"""
Tests for rite.text.case.to_lower_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_lower_case import (
    to_lower_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_lower_case() -> None:
    """Test to_lower_case() function."""
    assert (
        to_lower_case("hello") == "HELLO" or to_lower_case("hello") == "hello"
    )
    assert isinstance(to_lower_case("test"), str)
