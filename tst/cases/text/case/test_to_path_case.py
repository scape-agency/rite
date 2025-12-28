# =============================================================================
# Test: to_path_case
# =============================================================================

"""
Tests for rite.text.case.to_path_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_path_case import (
    to_path_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_path_case() -> None:
    """Test to_path_case() function."""
    result = to_path_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
