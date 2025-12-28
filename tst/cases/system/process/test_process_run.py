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
    from pathlib import Path
    import subprocess
    import tempfile

    # Test successful command
    code, out, err = process_run(["echo", "hello"])
    assert code == 0
    assert out == "hello"
    assert err == ""

    # Test failing command
    code, out, err = process_run(["false"])
    assert code != 0

    # Test command with stderr
    code, out, err = process_run(["sh", "-c", "echo err >&2"])
    assert "err" in err

    # Test command with working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        code, out, err = process_run(["pwd"], cwd=tmpdir)
        assert code == 0
        assert tmpdir in out

    # Test command with cwd as string
    with tempfile.TemporaryDirectory() as tmpdir:
        code, out, err = process_run(["pwd"], cwd=str(tmpdir))
        assert code == 0

    # Test command with cwd as Path
    with tempfile.TemporaryDirectory() as tmpdir:
        code, out, err = process_run(["pwd"], cwd=Path(tmpdir))
        assert code == 0

    # Test check=False (default)
    code, out, err = process_run(["false"], check=False)
    assert code != 0

    # Test check=True raises exception
    with pytest.raises(subprocess.CalledProcessError):
        process_run(["false"], check=True)

    # Test both stdout and stderr
    code, out, err = process_run(["sh", "-c", "echo out; echo err >&2"])
    assert "out" in out
    assert "err" in err
