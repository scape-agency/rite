# =============================================================================
# Test: converter_string_to_bool
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_bool.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_bool import (
    convert_string_to_bool,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        ("true", True),
        ("t", True),
        ("1", True),
        ("yes", True),
        ("y", True),
        ("false", False),
        ("f", False),
        ("0", False),
        ("no", False),
        ("n", False),
        ("", None),
        ("maybe", None),
        ("abc", None),
    ],
)
def test_convert_string_to_bool(value: str, expected: bool | None) -> None:
    """Test convert_string_to_bool() with various inputs."""
    assert convert_string_to_bool(value) == expected


def test_convert_string_to_bool_none_input() -> None:
    """Test with None input (line 36)."""
    assert convert_string_to_bool(None) is None


def test_convert_string_to_bool_whitespace() -> None:
    """Test with whitespace around values."""
    assert convert_string_to_bool("  true  ") is True
    assert convert_string_to_bool("  false  ") is False
    assert convert_string_to_bool("  YES  ") is True
