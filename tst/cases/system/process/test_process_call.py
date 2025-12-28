# =============================================================================
# Test: process_call
# =============================================================================

"""
Tests for rite.system.process.process_call.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.process.process_call import (
    process_call,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_process_call() -> None:
    """Test process_call() function."""
    from pathlib import Path
    import tempfile

    # Test successful command
    exitcode = process_call(["true"])
    assert exitcode == 0

    # Test failing command
    exitcode = process_call(["false"])
    assert exitcode != 0

    # Test command with working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        exitcode = process_call(["pwd"], cwd=tmpdir)
        assert exitcode == 0

    # Test command with cwd as string
    with tempfile.TemporaryDirectory() as tmpdir:
        exitcode = process_call(["pwd"], cwd=str(tmpdir))
        assert exitcode == 0

    # Test command with cwd as Path
    with tempfile.TemporaryDirectory() as tmpdir:
        exitcode = process_call(["pwd"], cwd=Path(tmpdir))
        assert exitcode == 0

    # Test simple echo command
    exitcode = process_call(["echo", "hello"])
    assert exitcode == 0

    # Test command with arguments
    exitcode = process_call(["sh", "-c", "exit 0"])
    assert exitcode == 0
