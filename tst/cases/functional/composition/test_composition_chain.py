# =============================================================================
# Test: composition_chain
# =============================================================================

"""
Tests for rite.functional.composition.composition_chain.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.composition.composition_chain import (
    composition_chain,
)

# =============================================================================
# Test Class: composition_chain
# =============================================================================


class Testcomposition_chain:
    """Tests for composition_chain class."""

    def test_instantiation(self) -> None:
        """Test composition_chain can be instantiated."""
        instance = composition_chain(42)
        assert instance is not None

    def test_pipe(self) -> None:
        """Test composition_chain.pipe() method."""
        instance = composition_chain(5)
        double = lambda x: x * 2
        result = instance.pipe(double)
        assert result.value() == 10

    def test_value(self) -> None:
        """Test composition_chain.value() method."""
        instance = composition_chain(42)
        assert instance.value() == 42
