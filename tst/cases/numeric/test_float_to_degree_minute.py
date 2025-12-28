# =============================================================================
# Test: float_to_degree_minute
# =============================================================================

"""
Tests for rite.numeric.float_to_degree_minute.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.numeric.float_to_degree_minute import (
    float_to_degree_minute,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_float_to_degree_minute_positive() -> None:
    """Test positive values conversion to degree and minute."""
    assert float_to_degree_minute(12.5) == (12, 30.0)
    assert float_to_degree_minute(0.0) == (0, 0.0)


def test_float_to_degree_minute_negative() -> None:
    """Test negative values keep sign when absolute is False."""
    assert float_to_degree_minute(-12.5) == (-12, 30.0)


def test_float_to_degree_minute_absolute() -> None:
    """Test negative values are made absolute when requested."""
    assert float_to_degree_minute(-12.5, absolute=True) == (12, 30.0)
