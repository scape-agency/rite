# =============================================================================
# Test: slugify
# =============================================================================

"""
Tests for rite.text.slug.slugify.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.slug.slugify import (
    slugify,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_slugify() -> None:
    """Test slugify() function."""
    # Basic slugify
    assert slugify("Hello World!") == "hello-world"

    # With custom delimiter
    assert slugify("Café au Lait", delimiter="_") == "cafe_au_lait"

    # With max length
    assert slugify("Hello World", max_length=8) == "hello-wo"

    # With custom replacements
    assert (
        slugify("Hello & World", custom_replacements={"&": "and"})
        == "hello-and-world"
    )

    # Without lowercase
    assert slugify("Hello World", lowercase=False) == "Hello-World"
