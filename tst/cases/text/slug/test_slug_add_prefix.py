# =============================================================================
# Test: slug_add_prefix
# =============================================================================

"""
Tests for rite.text.slug.slug_add_prefix.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.slug.slug_add_prefix import (
    add_slug_prefix,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_add_slug_prefix() -> None:
    """Test add_slug_prefix() function."""
    # Basic prefix
    assert add_slug_prefix("world", "hello") == "hello-world"

    # With custom delimiter
    assert add_slug_prefix("world", "hello", delimiter="_") == "hello_world"

    # With empty prefix
    assert add_slug_prefix("world", "") == "world"
