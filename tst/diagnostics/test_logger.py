# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Tests for Logger Module
=======================

This test suite verifies the functionality of the `Logger` class, a configurable
logging utility for applications.

Tested Features:
----------------
- Log messages to console and file.
- Verify correct log levels for debug, info, warning, error, and critical.
- Clear the log file content.
- Handle invalid log levels.

Dependencies:
-------------
- `pytest` for writing and executing tests.
- `os` and `tempfile` for temporary file handling.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import os
import tempfile

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics import Logger

# =============================================================================
# Test Cases
# =============================================================================


def test_logger_initialization():
    """
    Test initialization of the Logger with console and file logging.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_log = os.path.join(tmpdir, "test.log")
        logger = Logger(name="TestLogger", log_file=temp_log)
        assert logger.log_file == temp_log, "Log file path should match."
        # Close handlers before directory cleanup
        for handler in logger.logger.handlers[:]:
            handler.close()
            logger.logger.removeHandler(handler)


def test_logging_levels():
    """
    Test logging at various levels (debug, info, warning, error, critical).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_log = os.path.join(tmpdir, "test.log")
        logger = Logger(name="TestLoggerLevels", log_file=temp_log)

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

        # Flush handlers
        for handler in logger.logger.handlers:
            handler.flush()

        with open(temp_log, "r", encoding="utf-8") as log_file:
            log_content = log_file.read()

        assert (
            "Debug message" in log_content
        ), "Debug message should be logged."
        assert "Info message" in log_content, "Info message should be logged."
        assert (
            "Warning message" in log_content
        ), "Warning message should be logged."
        assert (
            "Error message" in log_content
        ), "Error message should be logged."
        assert (
            "Critical message" in log_content
        ), "Critical message should be logged."

        # Close handlers before directory cleanup
        for handler in logger.logger.handlers[:]:
            handler.close()
            logger.logger.removeHandler(handler)


def test_invalid_log_level():
    """
    Test logging with an invalid log level.
    """
    logger = Logger(name="TestLogger")

    with pytest.raises(ValueError, match="Invalid log level: invalid"):
        logger.log("invalid", "This should raise an error")


def test_clear_log():
    """
    Test clearing the log file content.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_log = os.path.join(tmpdir, "test.log")
        logger = Logger(name="TestLoggerClear", log_file=temp_log)

        logger.info("Test message")
        logger.clear_log()

        with open(temp_log, "r", encoding="utf-8") as log_file:
            log_content = log_file.read()

        assert (
            log_content == ""
        ), "Log file should be cleared after calling clear_log."

        # Close handlers before directory cleanup
        for handler in logger.logger.handlers[:]:
            handler.close()
            logger.logger.removeHandler(handler)


def test_console_logging(capsys):
    """
    Test console logging output.
    """
    logger = Logger(name="TestLogger")

    logger.info("Console info message")
    captured = capsys.readouterr()

    assert (
        "Console info message" in captured.err
    ), "Console logging should capture messages."


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main()
