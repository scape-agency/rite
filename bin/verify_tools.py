#!/usr/bin/env python3
# =============================================================================
# Tool Verification Script
# =============================================================================

"""
Verify Tool Configuration
==========================

This script verifies that all development tools are properly configured
and working correctly in the Rite project.
"""

# Import | Future
from __future__ import annotations

# Import | Standard Library
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> tuple[bool, str]:
    """
    Run a command and return success status and output.

    Args:
        cmd: Command to run as list of strings.
        description: Human-readable description of the command.

    Returns:
        Tuple of (success: bool, output: str).
    """
    print(f"\n{'='*70}")
    print(f"Testing: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*70}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

        output = result.stdout + result.stderr
        print(output[:500])  # Print first 500 chars

        if result.returncode == 0:
            print(f"✓ {description} - PASSED")
            return True, output
        else:
            print(f"✗ {description} - FAILED (exit code: {result.returncode})")
            return False, output

    except FileNotFoundError:
        print(f"✗ {description} - NOT FOUND")
        return False, "Command not found"
    except Exception as e:
        print(f"✗ {description} - ERROR: {e}")
        return False, str(e)


def main() -> int:
    """Run all verification tests."""
    print("\n" + "=" * 70)
    print("Rite Project - Tool Configuration Verification")
    print("=" * 70)

    # Change to project root
    project_root = Path(__file__).parent
    print(f"\nProject root: {project_root}")

    results: dict[str, bool] = {}

    # Test Black
    success, _ = run_command(
        ["poetry", "run", "black", "--version"],
        "Black - Code Formatter",
    )
    results["Black"] = success

    # Test isort
    success, _ = run_command(
        ["poetry", "run", "isort", "--version"],
        "isort - Import Sorter",
    )
    results["isort"] = success

    # Test Flake8
    success, _ = run_command(
        ["poetry", "run", "flake8", "--version"],
        "Flake8 - Linter",
    )
    results["Flake8"] = success

    # Test Pylint
    success, _ = run_command(
        ["poetry", "run", "pylint", "--version"],
        "Pylint - Static Analyzer",
    )
    results["Pylint"] = success

    # Test Mypy
    success, _ = run_command(
        ["poetry", "run", "mypy", "--version"],
        "Mypy - Type Checker",
    )
    results["Mypy"] = success

    # Test Pytest
    success, _ = run_command(
        ["poetry", "run", "pytest", "--version"],
        "Pytest - Test Framework",
    )
    results["Pytest"] = success

    # Test Black on sample file
    success, _ = run_command(
        [
            "poetry",
            "run",
            "black",
            "--check",
            "src/rite/crypto/uuid/__init__.py",
        ],
        "Black - Check Sample File",
    )
    results["Black Check"] = success

    # Test isort on sample file
    success, _ = run_command(
        [
            "poetry",
            "run",
            "isort",
            "--check-only",
            "src/rite/crypto/uuid/__init__.py",
        ],
        "isort - Check Sample File",
    )
    results["isort Check"] = success

    # Test Flake8 on sample file
    success, _ = run_command(
        ["poetry", "run", "flake8", "src/rite/crypto/uuid/__init__.py"],
        "Flake8 - Lint Sample File",
    )
    results["Flake8 Lint"] = success

    # Test Mypy on sample file
    success, _ = run_command(
        ["poetry", "run", "mypy", "src/rite/crypto/uuid/__init__.py"],
        "Mypy - Type Check Sample File",
    )
    results["Mypy Check"] = success

    # Test Pylint on sample file
    success, _ = run_command(
        [
            "poetry",
            "run",
            "pylint",
            "--rcfile=.pylintrc",
            "src/rite/crypto/uuid/__init__.py",
        ],
        "Pylint - Analyze Sample File",
    )
    results["Pylint Analyze"] = success

    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for name, success in results.items():
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{name:20} {status}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n✓ All tools are properly configured and working!")
        return 0
    else:
        print(
            f"\n✗ {total - passed} tool(s) failed. "
            "Please check the configuration."
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
