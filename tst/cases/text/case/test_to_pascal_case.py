# =============================================================================
# Test: to_pascal_case
# =============================================================================

"""
Tests for rite.text.case.to_pascal_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_pascal_case import (
    to_pascal_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_pascal_case() -> None:
    """Test to_pascal_case() function."""
    result = to_pascal_case("hello world")
    assert isinstance(result, str)
    assert len(result) > 0
