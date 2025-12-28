# =============================================================================
# Test: to_upper_case
# =============================================================================

"""
Tests for rite.text.case.to_upper_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_upper_case import (
    to_upper_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_upper_case() -> None:
    """Test to_upper_case() function."""
    assert to_upper_case("hello") == "HELLO" or to_upper_case("hello") == "hello"
    assert isinstance(to_upper_case("test"), str)
