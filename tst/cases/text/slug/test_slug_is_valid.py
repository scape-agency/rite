# =============================================================================
# Test: slug_is_valid
# =============================================================================

"""
Tests for rite.text.slug.slug_is_valid.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.slug.slug_is_valid import (
    is_valid_slug,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_is_valid_slug() -> None:
    """Test is_valid_slug() function."""
    # Valid slugs
    assert is_valid_slug("hello-world") is True
    assert is_valid_slug("test123") is True
    
    # Invalid slugs
    assert is_valid_slug("Hello-World") is False  # uppercase
    assert is_valid_slug("-hello-world") is False  # starts with delimiter
    assert is_valid_slug("hello-world-") is False  # ends with delimiter
    assert is_valid_slug("hello--world") is False  # double delimiter
