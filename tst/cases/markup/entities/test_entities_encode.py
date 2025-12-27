# =============================================================================
# Test: entities_encode
# =============================================================================

"""
Tests for rite.markup.entities.entities_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.entities.entities_encode import (
    entities_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,ascii_only",
    [
        ("café", False),
        ("hello", False),
        ("<tag>", False),
        ("&", False),
    ],
)
def test_entities_encode(text: str, ascii_only: bool) -> None:
    """Test entities_encode() with various inputs."""
    result = entities_encode(text, ascii_only)
    # Just verify it returns a string
    assert isinstance(result, str)
    # Verify the result is entity-encoded (contains & or &#)
    if text != "hello":
        assert "&" in result
