# =============================================================================
# Test: logging_structured
# =============================================================================

"""
Tests for rite.diagnostics.logging.logging_structured.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.diagnostics.logging.logging_structured import (
    logging_structured,
    _JSONFormatter,
    _KeyValueFormatter,
)


# =============================================================================
# Test Class: _JSONFormatter
# =============================================================================


class Test_JSONFormatter:
    """Tests for _JSONFormatter class."""

    def test_instantiation(self) -> None:
        """Test _JSONFormatter can be instantiated."""
        # TODO: Implement test
        instance = _JSONFormatter()
        assert instance is not None

    def test_format(self) -> None:
        """Test _JSONFormatter.format() method."""
        # TODO: Implement test
        instance = _JSONFormatter()
        # result = instance.format()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Class: _KeyValueFormatter
# =============================================================================


class Test_KeyValueFormatter:
    """Tests for _KeyValueFormatter class."""

    def test_instantiation(self) -> None:
        """Test _KeyValueFormatter can be instantiated."""
        # TODO: Implement test
        instance = _KeyValueFormatter()
        assert instance is not None

    def test_format(self) -> None:
        """Test _KeyValueFormatter.format() method."""
        # TODO: Implement test
        instance = _KeyValueFormatter()
        # result = instance.format()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_logging_structured() -> None:
    """Test logging_structured() function."""
    # TODO: Implement test
    # result = logging_structured(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

