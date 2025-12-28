# =============================================================================
# Test: case_to_emoji
# =============================================================================

"""
Tests for rite.text.converters.case_to_emoji.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_emoji import (
    to_emoji_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_emoji_case() -> None:
    """Test to_emoji_case() function."""
    result = to_emoji_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
