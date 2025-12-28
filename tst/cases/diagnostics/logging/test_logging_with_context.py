# =============================================================================
# Test: logging_with_context
# =============================================================================

"""
Tests for rite.diagnostics.logging.logging_with_context.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import logging

# Import | Local Modules
from rite.diagnostics.logging.logging_with_context import (
    logging_with_context,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_logging_with_context_creates_adapter() -> None:
    """Test logging_with_context creates a LoggerAdapter."""
    adapter = logging_with_context("test", request_id="123")
    assert adapter is not None
    assert isinstance(adapter, logging.LoggerAdapter)


def test_logging_with_context_single_context() -> None:
    """Test logging_with_context with single context value."""
    adapter = logging_with_context("test", request_id="req123")
    assert adapter is not None
    assert adapter.extra is not None
    assert adapter.extra["request_id"] == "req123"


def test_logging_with_context_multiple_context() -> None:
    """Test logging_with_context with multiple context values."""
    adapter = logging_with_context(
        "test", request_id="req123", user_id=456, ip="192.168.1.1"
    )
    assert adapter.extra is not None
    assert adapter.extra["request_id"] == "req123"
    assert adapter.extra["user_id"] == 456
    assert adapter.extra["ip"] == "192.168.1.1"


def test_logging_with_context_custom_level() -> None:
    """Test logging_with_context with custom logging level."""
    adapter = logging_with_context("test", level=logging.DEBUG)
    assert adapter.logger.level == logging.DEBUG


def test_logging_with_context_default_level() -> None:
    """Test logging_with_context uses default INFO level."""
    adapter = logging_with_context("test")
    assert adapter.logger.level == logging.INFO


def test_logging_with_context_no_context() -> None:
    """Test logging_with_context with no context values."""
    adapter = logging_with_context("test")
    assert adapter is not None
    assert adapter.extra == {}


def test_logging_with_context_creates_handler() -> None:
    """Test logging_with_context sets up handler."""
    adapter = logging_with_context("test_handler_creation", req_id="r1")
    assert len(adapter.logger.handlers) > 0


def test_logging_with_context_info_message() -> None:
    """Test logging an info message with context."""
    adapter = logging_with_context("test_info", request_id="abc123")
    # This should not raise
    adapter.info("Test message")


def test_logging_with_context_debug_message() -> None:
    """Test logging a debug message with context."""
    adapter = logging_with_context(
        "test_debug", level=logging.DEBUG, task="test"
    )
    adapter.debug("Debug message")


def test_logging_with_context_warning_message() -> None:
    """Test logging a warning message with context."""
    adapter = logging_with_context("test_warning", request_id="warn123")
    adapter.warning("Warning message")


def test_logging_with_context_error_message() -> None:
    """Test logging an error message with context."""
    adapter = logging_with_context("test_error", request_id="err123")
    adapter.error("Error message")
