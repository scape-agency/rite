# =============================================================================
# Test: converter_string_to_datetime
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_datetime.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.text.converters.converter_string_to_datetime import (
    convert_string_to_datetime,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_convert_string_to_datetime() -> None:
    """Test convert_string_to_datetime() with valid inputs."""
    # Test ISO format with timezone
    result = convert_string_to_datetime("2024-12-11T11:42:34+00:00")
    assert result is not None
    assert result.year == 2024
    assert result.month == 12
    assert result.day == 11

    # Test None input
    assert convert_string_to_datetime(None) is None

    # Test empty string
    assert convert_string_to_datetime("") is None

    # Test invalid format
    assert convert_string_to_datetime("not-a-date") is None


def test_convert_string_to_datetime_none_null() -> None:
    """Test with 'none' and 'null' strings (line 55)."""
    assert convert_string_to_datetime("none") is None
    assert convert_string_to_datetime("null") is None
    assert convert_string_to_datetime("None") is None
    assert convert_string_to_datetime("NULL") is None


def test_convert_string_to_datetime_space_format() -> None:
    """Test ISO format with space instead of T (line 63)."""
    result = convert_string_to_datetime("2024-12-11 11:42:34+00:00")
    assert result is not None
    assert result.year == 2024
    assert result.month == 12
    assert result.day == 11


def test_convert_string_to_datetime_naive() -> None:
    """Test naive datetime gets UTC timezone."""
    result = convert_string_to_datetime("2024-12-11T11:42:34")
    assert result is not None
    assert result.tzinfo is not None
