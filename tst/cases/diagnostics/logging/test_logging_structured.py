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
import json
import logging

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.logging.logging_structured import (
    _JSONFormatter,
    _KeyValueFormatter,
    logging_structured,
)

# =============================================================================
# Test Class: _JSONFormatter
# =============================================================================


class Test_JSONFormatter:
    """Tests for _JSONFormatter class."""

    def test_instantiation(self) -> None:
        """Test _JSONFormatter can be instantiated."""
        instance = _JSONFormatter()
        assert instance is not None

    def test_format_json(self) -> None:
        """Test _JSONFormatter formats as JSON."""
        formatter = _JSONFormatter()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test message",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        parsed = json.loads(result)
        assert parsed["message"] == "Test message"
        assert parsed["level"] == "INFO"
        assert parsed["logger"] == "test"

    def test_format_json_with_extras(self) -> None:
        """Test _JSONFormatter includes extra fields."""
        formatter = _JSONFormatter()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test",
            args=(),
            exc_info=None,
        )
        record.user_id = 123  # type: ignore
        result = formatter.format(record)
        parsed = json.loads(result)
        assert parsed["user_id"] == 123


# =============================================================================
# Test Class: _KeyValueFormatter
# =============================================================================


class Test_KeyValueFormatter:
    """Tests for _KeyValueFormatter class."""

    def test_instantiation(self) -> None:
        """Test _KeyValueFormatter can be instantiated."""
        instance = _KeyValueFormatter()
        assert instance is not None

    def test_format_key_value(self) -> None:
        """Test _KeyValueFormatter formats as key=value."""
        formatter = _KeyValueFormatter()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        assert "level=INFO" in result
        assert "logger=test" in result
        assert 'message="Test"' in result

    def test_format_key_value_with_extras(self) -> None:
        """Test _KeyValueFormatter includes extra fields."""
        formatter = _KeyValueFormatter()
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="test.py",
            lineno=1,
            msg="Test",
            args=(),
            exc_info=None,
        )
        record.duration_ms = 500  # type: ignore
        result = formatter.format(record)
        assert 'duration_ms="500"' in result


# =============================================================================
# Test Functions
# =============================================================================


def test_logging_structured_json() -> None:
    """Test logging_structured with JSON format."""
    logger = logging_structured("test", json_format=True)
    assert logger is not None
    assert isinstance(logger, logging.Logger)


def test_logging_structured_keyvalue() -> None:
    """Test logging_structured with key-value format."""
    logger = logging_structured("test", json_format=False)
    assert logger is not None
    assert isinstance(logger, logging.Logger)


def test_logging_structured_default_level() -> None:
    """Test logging_structured uses default INFO level."""
    logger = logging_structured("test")
    assert logger.level == logging.INFO


def test_logging_structured_custom_level() -> None:
    """Test logging_structured with custom level."""
    logger = logging_structured("test", level=logging.DEBUG)
    assert logger.level == logging.DEBUG


def test_logging_structured_no_duplicate_handlers() -> None:
    """Test logging_structured doesn't add duplicate handlers."""
    logger1 = logging_structured("test")
    logger2 = logging_structured("test")

    assert logger1 is logger2
    assert len(logger1.handlers) == 1


def test_logging_structured_keyvalue_formatter() -> None:
    """Test logging_structured uses KeyValueFormatter (line 66)."""
    # Import | Standard Library
    import uuid

    # Use unique name to get fresh logger without existing handlers
    unique_name = f"test_kv_{uuid.uuid4().hex[:8]}"
    logger = logging_structured(unique_name, json_format=False)
    assert logger is not None
    assert len(logger.handlers) == 1
    # The formatter should be _KeyValueFormatter
    handler = logger.handlers[0]
    assert handler.formatter is not None
