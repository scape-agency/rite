# =============================================================================
# Test: process_run
# =============================================================================

"""
Tests for rite.system.process.process_run.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.process.process_run import (
    process_run,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_process_run() -> None:
    """Test process_run() function."""
    # Import | Standard Library
    import os
    from pathlib import Path
    import subprocess
    import sys
    import tempfile

    # Test successful command - use platform-agnostic approach
    if sys.platform == "win32":
        code, out, err = process_run(["cmd", "/c", "echo hello"])
    else:
        code, out, err = process_run(["echo", "hello"])
    assert code == 0
    assert "hello" in out

    # Test failing command
    if sys.platform == "win32":
        code, out, err = process_run(["cmd", "/c", "exit 1"])
    else:
        code, out, err = process_run(["false"])
    assert code != 0

    # Test command with stderr
    if sys.platform == "win32":
        code, out, err = process_run(["cmd", "/c", "echo err >&2"])
    else:
        code, out, err = process_run(["sh", "-c", "echo err >&2"])
    assert "err" in err

    # Test command with working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            code, out, err = process_run(["cmd", "/c", "cd"], cwd=tmpdir)
        else:
            code, out, err = process_run(["pwd"], cwd=tmpdir)
        assert code == 0
        # Normalize path comparison for cross-platform
        assert os.path.normcase(os.path.realpath(tmpdir)) in os.path.normcase(
            os.path.realpath(out.strip())
        )

    # Test command with cwd as string
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            code, out, err = process_run(["cmd", "/c", "cd"], cwd=str(tmpdir))
        else:
            code, out, err = process_run(["pwd"], cwd=str(tmpdir))
        assert code == 0

    # Test command with cwd as Path
    with tempfile.TemporaryDirectory() as tmpdir:
        if sys.platform == "win32":
            code, out, err = process_run(["cmd", "/c", "cd"], cwd=Path(tmpdir))
        else:
            code, out, err = process_run(["pwd"], cwd=Path(tmpdir))
        assert code == 0

    # Test check=False (default)
    if sys.platform == "win32":
        code, out, err = process_run(["cmd", "/c", "exit 1"], check=False)
    else:
        code, out, err = process_run(["false"], check=False)
    assert code != 0

    # Test check=True raises exception
    with pytest.raises(subprocess.CalledProcessError):
        if sys.platform == "win32":
            process_run(["cmd", "/c", "exit 1"], check=True)
        else:
            process_run(["false"], check=True)

    # Test both stdout and stderr
    if sys.platform == "win32":
        code, out, err = process_run(["cmd", "/c", "echo out && echo err >&2"])
    else:
        code, out, err = process_run(["sh", "-c", "echo out; echo err >&2"])
    assert "out" in out
    assert "err" in err
