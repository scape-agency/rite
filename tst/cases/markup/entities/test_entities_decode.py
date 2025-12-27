# =============================================================================
# Test: entities_decode
# =============================================================================

"""
Tests for rite.markup.entities.entities_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.entities.entities_decode import (
    entities_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,expected",
    [
        ("caf&#233;", "café"),
        ("hello", "hello"),
        ("&lt;tag&gt;", "<tag>"),
        ("&amp;", "&"),
        ("&quot;", '"'),
    ],
)
def test_entities_decode(text: str, expected: str) -> None:
    """Test entities_decode() with various entities."""
    assert entities_decode(text) == expected
