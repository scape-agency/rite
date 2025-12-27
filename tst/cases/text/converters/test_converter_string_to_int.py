# =============================================================================
# Test: converter_string_to_int
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_int.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_int import (
    convert_string_to_int,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        ("123", 123),
        ("0", 0),
        ("-42", -42),
        ("999", 999),
        ("", None),
        ("abc", None),
        ("12.34", None),
    ],
)
def test_convert_string_to_int(value: str, expected: int | None) -> None:
    """Test convert_string_to_int() with various inputs."""
    assert convert_string_to_int(value) == expected
