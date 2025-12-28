# =============================================================================
# Test: run_command
# =============================================================================

"""
Tests for rite.system.run_command.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import subprocess

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.run_command import (
    run_command,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_run_command() -> None:
    """Test run_command() function."""
    # Import | Standard Library
    from pathlib import Path
    import tempfile

    # Test simple command
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(["echo", "hello"], cwd)
        assert returncode == 0
        assert "hello" in stdout

    # Test command with no output
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(["true"], cwd)
        assert returncode == 0

    # Test failing command
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(["false"], cwd)
        assert returncode != 0

    # Test check=False (default)
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(
            ["sh", "-c", "exit 1"], cwd, check=False
        )
        assert returncode == 1

    # Test check=True raises on failure
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        with pytest.raises(subprocess.CalledProcessError):
            run_command(["false"], cwd, check=True)

    # Test command with stderr output
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(
            ["sh", "-c", "echo error >&2"], cwd
        )
        assert "error" in stderr

    # Test command with both stdout and stderr
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = Path(tmpdir)
        returncode, stdout, stderr = run_command(
            ["sh", "-c", "echo out; echo err >&2"], cwd
        )
        assert "out" in stdout
        assert "err" in stderr
