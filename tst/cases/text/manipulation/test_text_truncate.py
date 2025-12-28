# =============================================================================
# Test: text_truncate
# =============================================================================

"""
Tests for rite.text.manipulation.text_truncate.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.manipulation.text_truncate import (
    text_truncate,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_text_truncate() -> None:
    """Test text_truncate() function."""
    result = text_truncate("hello world", 5)
    assert isinstance(result, str)
    assert len(result) <= 5
