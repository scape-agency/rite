# =============================================================================
# Test: slug_unique
# =============================================================================

"""
Tests for rite.text.slug.slug_unique.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.slug.slug_unique import (
    unique_slug,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_unique_slug() -> None:
    """Test unique_slug() function."""
    # Unique slug (not in existing)
    assert unique_slug("hello-world", set()) == "hello-world"
    
    # Slug exists once
    assert unique_slug("hello-world", {"hello-world"}) == "hello-world-1"
    
    # Multiple conflicts
    assert unique_slug("hello-world", {"hello-world", "hello-world-1"}) == "hello-world-2"
    
    # With list input
    assert unique_slug("hello-world", ["hello-world"]) == "hello-world-1"
