# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Rite - Command Run Module

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import subprocess
from pathlib import Path
from typing import List, Tuple

# Import | Libraries

# Import | Local Modules

# =============================================================================
# Classes
# =============================================================================


def run_command(
    cmd: list[str],
    cwd: Path,
    check: bool = False,
) -> tuple[int, str, str]:
    """
    Run a command in a subprocess and return the result.

    Args:
        cmd: The command to run.
        cwd: The working directory to run the command in.
        check: Whether to check the return code.

    Returns:
        A tuple containing the return code, stdout, and stderr.

    """

    # Run the command
    p = subprocess.Popen(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Get the output and error
    out, err = p.communicate()

    # Check the return code
    if check and p.returncode != 0:
        raise subprocess.CalledProcessError(
            p.returncode,
            cmd,
            out,
            err,
        )

    # Return the result
    return p.returncode, out.strip(), err.strip()


# def is_git_repo(path: Path) -> bool:
#     return (path / ".git").is_dir()

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "run_command",
]
