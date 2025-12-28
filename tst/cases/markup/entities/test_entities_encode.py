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


def test_entities_encode_ascii_only() -> None:
    """Test entities_encode with ascii_only=True (line 53)."""
    result = entities_encode("café", ascii_only=True)
    # 'c', 'a', 'f' should stay as is, 'é' should be encoded
    assert result.startswith("caf")
    assert "&#" in result  # é encoded


def test_entities_encode_all_ascii() -> None:
    """Test entities_encode with all ASCII chars and ascii_only=True."""
    result = entities_encode("hello", ascii_only=True)
    # All ASCII should stay as is
    assert result == "hello"
