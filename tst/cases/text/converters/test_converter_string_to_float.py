# =============================================================================
# Test: converter_string_to_float
# =============================================================================

"""
Tests for rite.text.converters.converter_string_to_float.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.converter_string_to_float import (
    convert_string_to_float,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        ("3.14", 3.14),
        ("0.0", 0.0),
        ("-2.5", -2.5),
        ("100", 100.0),
        ("", None),
        ("abc", None),
        ("1.2.3", None),
    ],
)
def test_convert_string_to_float(value: str, expected: float | None) -> None:
    """Test convert_string_to_float() with various inputs."""
    assert convert_string_to_float(value) == expected
