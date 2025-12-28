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

# Import | Standard Library
import logging

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
        instance = _ColorFormatter()
        assert instance is not None

    def test_format_with_debug(self) -> None:
        """Test _ColorFormatter formats debug level."""
        fmt = "%(levelname)s - %(message)s"
        formatter = _ColorFormatter(fmt)
        record = logging.LogRecord(
            name="test",
            level=logging.DEBUG,
            pathname="test.py",
            lineno=1,
            msg="Debug message",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        assert "\033[36m" in result  # Cyan color
        assert "DEBUG" in result

    def test_format_with_error(self) -> None:
        """Test _ColorFormatter formats error level."""
        fmt = "%(levelname)s - %(message)s"
        formatter = _ColorFormatter(fmt)
        record = logging.LogRecord(
            name="test",
            level=logging.ERROR,
            pathname="test.py",
            lineno=1,
            msg="Error message",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        assert "\033[31m" in result  # Red color
        assert "ERROR" in result


# =============================================================================
# Test Functions
# =============================================================================


def test_logging_to_console_creates_logger() -> None:
    """Test logging_to_console creates a logger."""
    logger = logging_to_console("test")
    assert logger is not None
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test"


def test_logging_to_console_default_format() -> None:
    """Test logging_to_console uses default format."""
    logger = logging_to_console("test")
    assert logger is not None
    assert len(logger.handlers) > 0


def test_logging_to_console_custom_format() -> None:
    """Test logging_to_console with custom format."""
    custom_format = "%(name)s - %(message)s"
    logger = logging_to_console("test", format_string=custom_format)
    assert logger is not None
    assert isinstance(logger, logging.Logger)


def test_logging_to_console_with_colorize() -> None:
    """Test logging_to_console with colorize enabled."""
    logger = logging_to_console("test_colorize", colorize=True)
    assert logger is not None
    assert isinstance(logger.handlers[0].formatter, _ColorFormatter)


def test_logging_to_console_without_colorize() -> None:
    """Test logging_to_console with colorize disabled."""
    logger = logging_to_console("test", colorize=False)
    assert logger is not None
    assert isinstance(logger.handlers[0].formatter, logging.Formatter)
    assert not isinstance(logger.handlers[0].formatter, _ColorFormatter)


def test_logging_to_console_custom_level() -> None:
    """Test logging_to_console with custom logging level."""
    logger = logging_to_console("test", level=logging.DEBUG)
    assert logger.level == logging.DEBUG


def test_logging_to_console_no_duplicate_handlers() -> None:
    """Test logging_to_console doesn't add duplicate handlers."""
    logger1 = logging_to_console("test")
    logger2 = logging_to_console("test")

    # Should be the same logger
    assert logger1 is logger2
    # Should not have duplicate handlers
    assert len(logger1.handlers) == 1
