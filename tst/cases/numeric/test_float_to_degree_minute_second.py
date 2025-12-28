# =============================================================================
# Test: float_to_degree_minute_second
# =============================================================================

"""
Tests for rite.numeric.float_to_degree_minute_second.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.numeric.float_to_degree_minute_second import (
    float_to_degree_minute_second,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_float_to_degree_minute_second_positive() -> None:
    """Test positive values conversion to degree, minute, and second.""""
    assert float_to_degree_minute_second(12.5) == (12, 30, 0.0)
    assert float_to_degree_minute_second(0.0) == (0, 0, 0.0)


def test_float_to_degree_minute_second_negative() -> None:
    """Test negative values keep sign when absolute is False.""""
    assert float_to_degree_minute_second(-12.5) == (-12, 30, 0.0)


def test_float_to_degree_minute_second_absolute() -> None:
    """Test negative values are made absolute when requested.""""
    assert float_to_degree_minute_second(-12.5, absolute=True) == (12, 30, 0.0)

