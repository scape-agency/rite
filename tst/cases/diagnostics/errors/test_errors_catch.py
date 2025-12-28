# =============================================================================
# Test: errors_catch
# =============================================================================

"""
Tests for rite.diagnostics.errors.errors_catch.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.errors.errors_catch import (
    errors_catch,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_errors_catch() -> None:
    """Test errors_catch() context manager."""
    # Test catching exception silently
    with errors_catch():
        1 / 0

    # Test catching specific exception
    with errors_catch(exceptions=(ValueError,)):
        raise ValueError("test error")

    # Test catching multiple exception types
    with errors_catch(exceptions=(ValueError, KeyError)):
        raise KeyError("test")

    # Test with handler function
    handler_called = False

    def handler(e: Exception) -> None:
        nonlocal handler_called
        handler_called = True

    with errors_catch(handler=handler):
        raise RuntimeError("test")

    assert handler_called

    # Test reraise=True
    with pytest.raises(ValueError):
        with errors_catch(reraise=True):
            raise ValueError("reraised")

    # Test not catching non-matching exception
    with pytest.raises(TypeError):
        with errors_catch(exceptions=(ValueError,)):
            raise TypeError("not caught")

    # Test with logger
    # Import | Standard Library
    import logging

    logger = logging.getLogger(__name__)
    with errors_catch(logger=logger):
        raise RuntimeError("logged error")

    # Test exception not raised if not in tuple
    with pytest.raises(ZeroDivisionError):
        with errors_catch(exceptions=(ValueError,)):
            1 / 0
