# =============================================================================
# Test: logger
# =============================================================================

"""
Tests for rite.diagnostics.logger.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.logger import (
    Logger,
)

# =============================================================================
# Test Class: Logger
# =============================================================================


class TestLogger:
    """Tests for Logger class."""

    def test_instantiation(self) -> None:
        """Test Logger can be instantiated."""
        instance = Logger("test_logger")
        assert instance is not None
        assert instance.logger.name == "test_logger"

    def test_log(self) -> None:
        """Test Logger.log() method."""
        instance = Logger("test_logger")
        instance.log("info", "Test message")
        # Should not raise

    def test_debug(self) -> None:
        """Test Logger.debug() method."""
        instance = Logger("test_logger")
        instance.debug("Debug message")
        # Should not raise

    def test_info(self) -> None:
        """Test Logger.info() method."""
        instance = Logger("test_logger")
        instance.info("Info message")
        # Should not raise

    def test_warning(self) -> None:
        """Test Logger.warning() method."""
        instance = Logger("test_logger")
        instance.warning("Warning message")
        # Should not raise

    def test_error(self) -> None:
        """Test Logger.error() method."""
        instance = Logger("test_logger")
        instance.error("Error message")
        # Should not raise

    def test_critical(self) -> None:
        """Test Logger.critical() method."""
        instance = Logger("test_logger")
        instance.critical("Critical message")
        # Should not raise

    def test_clear_log(self) -> None:
        """Test Logger.clear_log() method."""
        # Import | Standard Library
        import tempfile

        tmp = tempfile.NamedTemporaryFile(delete=False)
        instance = Logger("test_logger", log_file=tmp.name)
        instance.info("Test message")
        instance.clear_log()
        # Should not raise
