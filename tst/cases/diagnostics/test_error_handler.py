# =============================================================================
# Test: error_handler
# =============================================================================

"""
Tests for rite.diagnostics.error_handler.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.error_handler import (
    ErrorHandler,
)

# =============================================================================
# Test Class: ErrorHandler
# =============================================================================


class TestErrorHandler:
    """Tests for ErrorHandler class."""

    def test_instantiation(self, tmp_path) -> None:
        """Test ErrorHandler can be instantiated."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)
        assert instance is not None
        assert instance.log_file == log_file

    def test_log_error(self, tmp_path, capsys) -> None:
        """Test ErrorHandler.log_error() method."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)
        instance.log_error("Test error")
        captured = capsys.readouterr()
        assert "Error logged: Test error" in captured.out

    def test_raise_alert(self, tmp_path, capsys) -> None:
        """Test ErrorHandler.raise_alert() method."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)
        instance.raise_alert("Critical error")
        captured = capsys.readouterr()
        assert "ALERT: Critical error" in captured.out

    def test_retry_operation_success(self, tmp_path) -> None:
        """Test ErrorHandler.retry_operation() with successful operation."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)

        def success_op():
            return True

        result = instance.retry_operation(success_op, retries=3)
        assert result is True

    def test_retry_operation_failure(self, tmp_path) -> None:
        """Test ErrorHandler.retry_operation() with failing operation."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)

        def failing_op():
            raise RuntimeError("Test failure")

        result = instance.retry_operation(failing_op, retries=2, backoff=0.01)
        assert result is False

    def test_retry_operation_eventual_success(self, tmp_path) -> None:
        """Test ErrorHandler.retry_operation() with eventual success."""
        log_file = str(tmp_path / "test.log")
        instance = ErrorHandler(log_file=log_file)

        attempt_count = {"count": 0}

        def eventual_success():
            attempt_count["count"] += 1
            if attempt_count["count"] < 2:
                raise RuntimeError("First attempt fails")
            return True

        result = instance.retry_operation(
            eventual_success, retries=3, backoff=0.01
        )
        assert result is True
