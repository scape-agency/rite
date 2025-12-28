# =============================================================================
# Test: to_camel_case
# =============================================================================

"""
Tests for rite.text.case.to_camel_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_camel_case import (
    to_camel_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_camel_case() -> None:
    """Test to_camel_case() function."""
    result = to_camel_case("hello world")
    assert isinstance(result, str)
    assert len(result) > 0
