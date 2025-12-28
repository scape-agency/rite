# =============================================================================
# Test: to_dot_case
# =============================================================================

"""
Tests for rite.text.case.to_dot_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_dot_case import (
    to_dot_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_dot_case() -> None:
    """Test to_dot_case() function."""
    result = to_dot_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
