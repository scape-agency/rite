# =============================================================================
# Test: logging_to_file
# =============================================================================

"""
Tests for rite.diagnostics.logging.logging_to_file.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import logging
from pathlib import Path
import tempfile

# Import | Local Modules
from rite.diagnostics.logging.logging_to_file import (
    logging_to_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_logging_to_file_creates_logger() -> None:
    """Test logging_to_file creates a logger."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        logger = logging_to_file("test", str(log_file))
        assert logger is not None
        assert isinstance(logger, logging.Logger)
        assert logger.name == "test"


def test_logging_to_file_writes_to_file() -> None:
    """Test logging_to_file writes messages to file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        logger = logging_to_file("test_write", str(log_file))
        logger.info("Test message")
        # Flush and close handlers to ensure content is written and file released
        for handler in logger.handlers[:]:
            handler.flush()
            handler.close()
            logger.removeHandler(handler)

        content = log_file.read_text()
        assert "Test message" in content


def test_logging_to_file_respects_level() -> None:
    """Test logging_to_file respects logging level."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        logger = logging_to_file(
            "test_level", str(log_file), level=logging.WARNING
        )
        logger.debug("Debug message")
        logger.warning("Warning message")
        # Flush and close handlers to ensure content is written and file released
        for handler in logger.handlers[:]:
            handler.flush()
            handler.close()
            logger.removeHandler(handler)

        content = log_file.read_text()
        assert "Debug message" not in content
        assert "Warning message" in content


def test_logging_to_file_custom_format() -> None:
    """Test logging_to_file with custom format string."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        custom_format = "%(name)s - %(message)s"
        logger = logging_to_file(
            "test_format", str(log_file), format_string=custom_format
        )
        logger.info("Test")
        # Flush and close handlers to ensure content is written and file released
        for handler in logger.handlers[:]:
            handler.flush()
            handler.close()
            logger.removeHandler(handler)

        content = log_file.read_text()
        assert "test_format - Test" in content


def test_logging_to_file_rotation_params() -> None:
    """Test logging_to_file with rotation parameters."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        logger = logging_to_file(
            "test", str(log_file), max_bytes=1024, backup_count=3
        )
        assert logger is not None


def test_logging_to_file_no_duplicate_handlers() -> None:
    """Test logging_to_file doesn't add duplicate handlers."""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = Path(tmpdir) / "test.log"
        logger1 = logging_to_file("test", str(log_file))
        logger2 = logging_to_file("test", str(log_file))

        # Should be the same logger instance
        assert logger1 is logger2
        # Should not have duplicate handlers
        assert len(logger1.handlers) == 1
