# =============================================================================
# Test: string_clean
# =============================================================================

"""
Tests for rite.text.converters.string_clean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.string_clean import (
    string_clean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_string_clean() -> None:
    """Test string_clean() function."""
    result = string_clean("hello")
    assert isinstance(result, str)
    assert len(result) > 0
