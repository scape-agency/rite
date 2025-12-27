# =============================================================================
# Test: logging_to_console
# =============================================================================

"""
Tests for rite.diagnostics.logging.logging_to_console.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.logging.logging_to_console import (
    _ColorFormatter,
    logging_to_console,
)

# =============================================================================
# Test Class: _ColorFormatter
# =============================================================================


class Test_ColorFormatter:
    """Tests for _ColorFormatter class."""

    def test_instantiation(self) -> None:
        """Test _ColorFormatter can be instantiated."""
        # TODO: Implement test
        instance = _ColorFormatter()
        assert instance is not None

    def test_format(self) -> None:
        """Test _ColorFormatter.format() method."""
        # TODO: Implement test
        instance = _ColorFormatter()
        # result = instance.format()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_logging_to_console() -> None:
    """Test logging_to_console() function."""
    # TODO: Implement test
    # result = logging_to_console(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")
