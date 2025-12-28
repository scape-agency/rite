# =============================================================================
# Test: coordinates_from_degree_minute_second
# =============================================================================

"""
Tests for rite.numeric.coordinates.coordinates_from_degree_minute_second.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.numeric.coordinates.coordinates_from_degree_minute_second import (
    coordinates_from_degree_minute_second,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_coordinates_from_degree_minute_second_basic() -> None:
    """Test basic DMS to float conversion."""
    assert coordinates_from_degree_minute_second(12, 30, 0) == 12.5
    assert (
        coordinates_from_degree_minute_second(0, 0, 30) == 0.008333333333333333
    )


def test_coordinates_from_degree_minute_second_negative() -> None:
    """Test negative degrees are handled with sign on result."""
    result = coordinates_from_degree_minute_second(-12, 30, 30)
    assert result == -12.508333333333333
