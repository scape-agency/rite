# =============================================================================
# Test: CLI
# =============================================================================

"""
Tests for rite.cli module.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from io import StringIO
from pathlib import Path
import sys

# Import | Libraries
import pytest

# Import | Local Modules
from rite.cli import (
    cli_main,
    cmd_case,
    cmd_file_hash,
    cmd_hash,
    cmd_info,
    cmd_slug,
    cmd_uuid,
    create_parser,
)

# =============================================================================
# Test CLI Parser
# =============================================================================


def test_create_parser():
    """Test CLI parser creation."""
    parser = create_parser()
    assert parser is not None
    assert parser.prog == "rite"


# =============================================================================
# Test Commands
# =============================================================================


def test_cmd_info(capsys):
    """Test info command."""
    args = create_parser().parse_args(["info"])
    result = cmd_info(args)

    assert result == 0
    captured = capsys.readouterr()
    assert "rite v" in captured.out
    assert "collections" in captured.out


def test_cmd_hash_sha256(capsys):
    """Test hash command with SHA-256."""
    args = create_parser().parse_args(["hash", "test"])
    result = cmd_hash(args)

    assert result == 0
    captured = capsys.readouterr()
    assert len(captured.out.strip()) == 64  # SHA-256 hex length


def test_cmd_hash_md5(capsys):
    """Test hash command with MD5."""
    args = create_parser().parse_args(["hash", "test", "-a", "md5"])
    result = cmd_hash(args)

    assert result == 0
    captured = capsys.readouterr()
    assert len(captured.out.strip()) == 32  # MD5 hex length


def test_cmd_hash_invalid_algorithm(capsys):
    """Test hash command with invalid algorithm."""
    args = create_parser().parse_args(["hash", "test"])
    args.algorithm = "invalid"
    result = cmd_hash(args)

    assert result == 1
    captured = capsys.readouterr()
    assert "Unknown algorithm" in captured.err


def test_cmd_uuid_single(capsys):
    """Test UUID generation (single)."""
    args = create_parser().parse_args(["uuid"])
    result = cmd_uuid(args)

    assert result == 0
    captured = capsys.readouterr()
    output = captured.out.strip()
    # UUID format: 8-4-4-4-12
    assert len(output) == 36
    assert output.count("-") == 4


def test_cmd_uuid_multiple(capsys):
    """Test UUID generation (multiple)."""
    args = create_parser().parse_args(["uuid", "-n", "3"])
    result = cmd_uuid(args)

    assert result == 0
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert len(lines) == 3


def test_cmd_uuid_hex(capsys):
    """Test UUID generation in hex format."""
    args = create_parser().parse_args(["uuid", "--hex"])
    result = cmd_uuid(args)

    assert result == 0
    captured = capsys.readouterr()
    output = captured.out.strip()
    # Hex format: 32 characters, no dashes
    assert len(output) == 32
    assert "-" not in output


def test_cmd_uuid_invalid_count(capsys):
    """Test UUID with invalid count."""
    args = create_parser().parse_args(["uuid"])
    args.count = 0
    result = cmd_uuid(args)

    assert result == 1
    captured = capsys.readouterr()
    assert "Count must be at least 1" in captured.err


def test_cmd_slug(capsys):
    """Test slug generation."""
    args = create_parser().parse_args(["slug", "Hello World!"])
    result = cmd_slug(args)

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello-world"


def test_cmd_case_snake(capsys):
    """Test case conversion to snake_case."""
    args = create_parser().parse_args(["case", "HelloWorld", "-t", "snake"])
    result = cmd_case(args)

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello_world"


def test_cmd_case_camel(capsys):
    """Test case conversion to camelCase."""
    args = create_parser().parse_args(["case", "hello_world", "-t", "camel"])
    result = cmd_case(args)

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "helloWorld"


def test_cmd_case_pascal(capsys):
    """Test case conversion to PascalCase."""
    args = create_parser().parse_args(["case", "hello_world", "-t", "pascal"])
    result = cmd_case(args)

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "HelloWorld"


def test_cmd_case_kebab(capsys):
    """Test case conversion to kebab-case."""
    args = create_parser().parse_args(["case", "helloWorld", "-t", "kebab"])
    result = cmd_case(args)

    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello-world"


def test_cmd_case_invalid_type(capsys):
    """Test case conversion with invalid type."""
    args = create_parser().parse_args(["case", "test", "-t", "snake"])
    args.type = "invalid"
    result = cmd_case(args)

    assert result == 1
    captured = capsys.readouterr()
    assert "Unknown case type" in captured.err


def test_cmd_file_hash(capsys, tmp_path: Path):
    """Test file hashing."""
    # Create test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")

    args = create_parser().parse_args(["file-hash", str(test_file)])
    result = cmd_file_hash(args)

    assert result == 0
    captured = capsys.readouterr()
    assert len(captured.out.strip().split()[0]) == 64  # SHA-256 hash


def test_cmd_file_hash_nonexistent(capsys):
    """Test file hashing with nonexistent file."""
    args = create_parser().parse_args(["file-hash", "/nonexistent/file.txt"])
    result = cmd_file_hash(args)

    assert result == 1
    captured = capsys.readouterr()
    assert "File not found" in captured.err


def test_cmd_file_hash_md5(capsys, tmp_path: Path):
    """Test file hashing with MD5."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")

    args = create_parser().parse_args(
        ["file-hash", str(test_file), "-a", "md5"]
    )
    result = cmd_file_hash(args)

    assert result == 0
    captured = capsys.readouterr()
    assert len(captured.out.strip().split()[0]) == 32  # MD5 hash


# =============================================================================
# Test CLI Main
# =============================================================================


def test_cli_main_no_args(capsys, monkeypatch):
    """Test CLI with no arguments."""
    monkeypatch.setattr(sys, "argv", ["rite"])
    result = cli_main()

    assert result == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out.lower()


def test_cli_main_version(capsys, monkeypatch):
    """Test CLI version flag."""
    monkeypatch.setattr(sys, "argv", ["rite", "--version"])

    with pytest.raises(SystemExit) as exc:
        cli_main()

    assert exc.value.code == 0


def test_cli_main_info(capsys, monkeypatch):
    """Test CLI info command."""
    monkeypatch.setattr(sys, "argv", ["rite", "info"])
    result = cli_main()

    assert result == 0
    captured = capsys.readouterr()
    assert "rite v" in captured.out
