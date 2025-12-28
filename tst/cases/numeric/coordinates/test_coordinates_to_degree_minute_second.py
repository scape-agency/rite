# =============================================================================
# Test: coordinates_to_degree_minute_second
# =============================================================================

"""
Tests for rite.numeric.coordinates.coordinates_to_degree_minute_second.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.numeric.coordinates.coordinates_to_degree_minute_second import (
    coordinates_to_degree_minute_second,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_coordinates_to_degree_minute_second_positive() -> None:
    """Test positive values conversion to DMS format."""
    assert coordinates_to_degree_minute_second(12.5) == (12, 30, 0.0)
    assert coordinates_to_degree_minute_second(0.0) == (0, 0, 0.0)


def test_coordinates_to_degree_minute_second_negative() -> None:
    """Test negative values keep sign when absolute is False."""
    # Import | Libraries
    import pytest

    result = coordinates_to_degree_minute_second(-12.508333)
    assert result[0] == -12
    assert result[1] == 30
    assert result[2] == pytest.approx(29.9988, abs=0.001)


def test_coordinates_to_degree_minute_second_absolute() -> None:
    """Test negative values are made absolute when requested."""
    assert coordinates_to_degree_minute_second(-12.5, absolute=True) == (
        12,
        30,
        0.0,
    )
