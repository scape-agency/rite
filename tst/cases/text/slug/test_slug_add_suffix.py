# =============================================================================
# Test: slug_add_suffix
# =============================================================================

"""
Tests for rite.text.slug.slug_add_suffix.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.slug.slug_add_suffix import (
    add_slug_suffix,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_add_slug_suffix() -> None:
    """Test add_slug_suffix() function."""
    # Basic suffix
    assert add_slug_suffix("hello", "world") == "hello-world"
    
    # With custom delimiter
    assert add_slug_suffix("hello", "world", delimiter="_") == "hello_world"
    
    # With empty suffix
    assert add_slug_suffix("hello", "") == "hello"
