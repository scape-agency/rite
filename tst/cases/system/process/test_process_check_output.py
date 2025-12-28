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
    from pathlib import Path
    import subprocess
    import tempfile

    # Test successful command with output
    output = process_check_output(["echo", "hello"])
    assert output == "hello"

    # Test command with multiple lines
    output = process_check_output(["sh", "-c", "echo 'line1'; echo 'line2'"])
    assert "line1" in output
    assert "line2" in output

    # Test command with working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        output = process_check_output(["pwd"], cwd=tmpdir)
        assert tmpdir in output

    # Test command with cwd as string
    with tempfile.TemporaryDirectory() as tmpdir:
        output = process_check_output(["pwd"], cwd=str(tmpdir))
        assert len(output) > 0

    # Test command with cwd as Path
    with tempfile.TemporaryDirectory() as tmpdir:
        output = process_check_output(["pwd"], cwd=Path(tmpdir))
        assert len(output) > 0

    # Test failing command raises exception
    with pytest.raises(subprocess.CalledProcessError):
        process_check_output(["false"])

    # Test command output is stripped
    output = process_check_output(["echo", "test"])
    assert output == "test"
    assert not output.endswith("\n")
