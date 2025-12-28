# =============================================================================
# Test: sanitize_text
# =============================================================================

"""
Tests for rite.text.sanitize.sanitize_text.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.sanitize.sanitize_text import (
    sanitize,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_sanitize() -> None:
    """Test sanitize() function."""
    result = sanitize("hello")
    assert isinstance(result, str)
    assert len(result) > 0
