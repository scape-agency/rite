# =============================================================================
# Test: converter_string_to_binary
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_binary.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_binary import (
    convert_string_to_binary,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,expected",
    [
        ("A", "01000001"),
        ("AB", "01000001 01000010"),
        ("", ""),
        ("a", "01100001"),
    ],
)
def test_convert_string_to_binary(text: str, expected: str) -> None:
    """Test convert_string_to_binary() with various inputs."""
    assert convert_string_to_binary(text) == expected
