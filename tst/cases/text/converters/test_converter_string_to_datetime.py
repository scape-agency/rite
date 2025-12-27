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

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_datetime import (
    convert_string_to_datetime,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_convert_string_to_datetime() -> None:
    """Test convert_string_to_datetime() with valid inputs."""
    # Import | Standard Library
    from datetime import datetime

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
