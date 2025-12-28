# =============================================================================
# Test: to_constant_case
# =============================================================================

"""
Tests for rite.text.case.to_constant_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_constant_case import (
    to_constant_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_constant_case() -> None:
    """Test to_constant_case() function."""
    result = to_constant_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
