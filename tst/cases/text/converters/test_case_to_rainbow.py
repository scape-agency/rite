# =============================================================================
# Test: case_to_rainbow
# =============================================================================

"""
Tests for rite.text.converters.case_to_rainbow.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_rainbow import (
    to_rainbow_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_rainbow_case() -> None:
    """Test to_rainbow_case() function."""
    result = to_rainbow_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
