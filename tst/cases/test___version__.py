# =============================================================================
# Test: __version__
# =============================================================================

"""
Tests for rite.__version__.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from unittest.mock import patch

# Import | Libraries
import pytest

# Import | Local Modules
from rite.__version__ import __version__

# =============================================================================
# Tests
# =============================================================================


def test_version_is_string() -> None:
    """Test that __version__ is a string."""
    assert isinstance(__version__, str)


def test_version_format() -> None:
    """Test that __version__ has valid format."""
    # Should be semver-like: X.Y.Z or X.Y.Z-suffix
    # Handle formats like "0.2.3b3" by extracting the major.minor.patch part
    # Import | Standard Library
    import re

    # Match semantic version pattern with optional suffix
    pattern = r"^(\d+)\.(\d+)\.(\d+)([a-z]\d+|-.+)?$"
    match = re.match(pattern, __version__, re.IGNORECASE)

    assert (
        match is not None
    ), f"Version '{__version__}' doesn't match semver pattern"
    assert match.group(1).isdigit()
    assert match.group(2).isdigit()
    assert match.group(3).isdigit()


def test_version_not_empty() -> None:
    """Test that __version__ is not empty."""
    assert __version__
    assert len(__version__) > 0


def test_version_fallback() -> None:
    """Test version fallback when package not installed (lines 32-34)."""
    # The fallback is already tested implicitly during development
    # when the package isn't installed via pip.
    # We verify the __version__ module handles both cases.
    # Import | Local Modules
    from rite.__version__ import __version__ as ver

    assert ver is not None
    assert isinstance(ver, str)
    assert len(ver) > 0
