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
        # TODO: Implement test
        instance = composition_chain()
        assert instance is not None

    def test_pipe(self) -> None:
        """Test composition_chain.pipe() method."""
        # TODO: Implement test
        instance = composition_chain()
        # result = instance.pipe()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_value(self) -> None:
        """Test composition_chain.value() method."""
        # TODO: Implement test
        instance = composition_chain()
        # result = instance.value()
        # assert result is not None
        pytest.skip("Test not implemented")
