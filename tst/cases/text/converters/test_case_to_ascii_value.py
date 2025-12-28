# =============================================================================
# Test: case_to_ascii_value
# =============================================================================

"""
Tests for rite.text.converters.case_to_ascii_value.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_ascii_value import (
    to_ascii_value_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_ascii_value_case() -> None:
    """Test to_ascii_value_case() function."""
    result = to_ascii_value_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
