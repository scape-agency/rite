# =============================================================================
# Test: process_check_output
# =============================================================================

"""
Tests for rite.system.process.process_check_output.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.process.process_check_output import (
    process_check_output,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_process_check_output() -> None:
    """Test process_check_output() function."""
    # Import | Standard Library
    import os
    from pathlib import Path
    import subprocess
    import sys
    import tempfile

    # Test successful command with output
    if sys.platform == "win32":
        output = process_check_output(["cmd", "/c", "echo hello"])
    else:
        output = process_check_output(["echo", "hello"])
    assert "hello" in output

    # Test command with multiple lines
    if sys.platform == "win32":
        output = process_check_output(
            ["cmd", "/c", "echo line1 && echo line2"]
        )
    else:
        output = process_check_output(
            ["sh", "-c", "echo 'line1'; echo 'line2'"]
        )
    assert "line1" in output
    assert "line2" in output

    # Test command with working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            output = process_check_output(["cmd", "/c", "cd"], cwd=tmpdir)
        else:
            output = process_check_output(["pwd"], cwd=tmpdir)
        # Normalize path comparison for cross-platform
        assert os.path.normcase(os.path.realpath(tmpdir)) in os.path.normcase(
            os.path.realpath(output.strip())
        )

    # Test command with cwd as string
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            output = process_check_output(["cmd", "/c", "cd"], cwd=str(tmpdir))
        else:
            output = process_check_output(["pwd"], cwd=str(tmpdir))
        assert len(output) > 0

    # Test command with cwd as Path
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            output = process_check_output(
                ["cmd", "/c", "cd"], cwd=Path(tmpdir)
            )
        else:
            output = process_check_output(["pwd"], cwd=Path(tmpdir))
        assert len(output) > 0

    # Test failing command raises exception
    if sys.platform == "win32":
        with pytest.raises(subprocess.CalledProcessError):
            process_check_output(["cmd", "/c", "exit 1"])
    else:
        with pytest.raises(subprocess.CalledProcessError):
            process_check_output(["false"])

    # Test command output is stripped
    if sys.platform == "win32":
        output = process_check_output(["cmd", "/c", "echo test"])
    else:
        output = process_check_output(["echo", "test"])
    assert "test" in output
