#!/usr/bin/env python3
"""
Generate pytest test files for all source modules.

This script creates test files in tst/cases/ that mirror the structure
of src/rite/. Each test file includes:
- Proper imports
- Test class for each source class
- Test function for each source function
- Basic test structure following project conventions
"""

# Import | Future
from __future__ import annotations

# Import | Standard Library
import ast
from pathlib import Path


def get_module_info(
    file_path: Path,
) -> tuple[list[str], list[tuple[str, list[str]]]]:
    """
    Extract functions and classes from a Python file.

    Args:
        file_path: Path to the source file.

    Returns:
        Tuple of (functions, classes_with_methods).
        classes_with_methods is list of (class_name, [method_names]).
    """
    try:
        with open(file_path) as f:
            tree = ast.parse(f.read())

        functions = []
        classes = []

        # Only process top-level nodes
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and not node.name.startswith(
                "_"
            ):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        if (
                            not item.name.startswith("_")
                            or item.name == "__init__"
                        ):
                            methods.append(item.name)
                classes.append((node.name, methods))

        return functions, classes
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return [], []


def generate_test_content(
    src_file: Path,
    src_root: Path,
    functions: list[str],
    classes: list[tuple[str, list[str]]],
) -> str:
    """
    Generate test file content.

    Args:
        src_file: Source file path.
        src_root: Source root directory.
        functions: List of function names.
        classes: List of (class_name, methods) tuples.

    Returns:
        Test file content as string.
    """
    rel_path = src_file.relative_to(src_root)
    module_path = str(rel_path.with_suffix("")).replace("/", ".")
    import_path = f"rite.{module_path}"

    # Get module name for description
    module_name = src_file.stem

    content = f'''# =============================================================================
# Test: {module_name}
# =============================================================================

"""
Tests for {import_path}.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from {import_path} import (
'''

    # Add imports
    all_symbols = functions + [cls[0] for cls in classes]
    if all_symbols:
        for symbol in all_symbols:
            content += f"    {symbol},\n"
    else:
        content += "    # TODO: Add imports\n"

    content += ")\n\n"

    # Generate tests for classes
    for class_name, methods in classes:
        content += f'''
# =============================================================================
# Test Class: {class_name}
# =============================================================================


class Test{class_name}:
    """Tests for {class_name} class."""

    def test_instantiation(self) -> None:
        """Test {class_name} can be instantiated."""
        # TODO: Implement test
        instance = {class_name}()
        assert instance is not None

'''
        for method in methods:
            if method == "__init__":
                continue
            content += f'''    def test_{method}(self) -> None:
        """Test {class_name}.{method}() method."""
        # TODO: Implement test
        instance = {class_name}()
        # result = instance.{method}()
        # assert result is not None
        pytest.skip("Test not implemented")

'''

    # Generate tests for functions
    if functions:
        content += """
# =============================================================================
# Test Functions
# =============================================================================

"""
        for func in functions:
            content += f'''
def test_{func}() -> None:
    """Test {func}() function."""
    # TODO: Implement test
    # result = {func}(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

'''

    if not functions and not classes:
        content += '''
# =============================================================================
# Placeholder Test
# =============================================================================


def test_module_exists() -> None:
    """Test that module can be imported."""
    # This test passes if the import succeeds
    assert True
'''

    return content


def create_test_file(
    src_file: Path, src_root: Path, tst_root: Path, dry_run: bool = False
) -> bool:
    """
    Create a test file for a source file.

    Args:
        src_file: Source file path.
        src_root: Source root directory.
        tst_root: Test root directory.
        dry_run: If True, don't create files, just print what would be done.

    Returns:
        True if test was created/would be created, False otherwise.
    """
    # Calculate test file path
    rel_path = src_file.relative_to(src_root)
    test_file = tst_root / rel_path.parent / f"test_{rel_path.name}"

    # Skip if test already exists
    if test_file.exists():
        return False

    # Get module info
    functions, classes = get_module_info(src_file)

    # Generate content
    content = generate_test_content(src_file, src_root, functions, classes)

    if dry_run:
        print(f"Would create: {test_file}")
        return True

    # Create test file
    test_file.parent.mkdir(parents=True, exist_ok=True)
    with open(test_file, "w") as f:
        f.write(content)

    print(f"Created: {test_file}")
    return True


def main() -> None:
    """Generate all missing test files."""
    # Import | Standard Library
    import argparse

    parser = argparse.ArgumentParser(description="Generate pytest test files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without creating files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of files to generate (for testing)",
    )
    args = parser.parse_args()

    src_root = Path("src/rite")
    tst_root = Path("tst/cases")

    # Ensure tst/cases exists
    tst_root.mkdir(parents=True, exist_ok=True)
    (tst_root / "__init__.py").touch()

    created_count = 0
    skipped_count = 0

    # Process all source files
    for src_file in sorted(src_root.rglob("*.py")):
        if src_file.name == "__init__.py" or "__pycache__" in str(src_file):
            continue

        if args.limit and created_count >= args.limit:
            break

        if create_test_file(src_file, src_root, tst_root, args.dry_run):
            created_count += 1
        else:
            skipped_count += 1

    print(f"\nSummary:")
    print(f"  Created: {created_count}")
    print(f"  Skipped (already exist): {skipped_count}")
    print(f"  Total: {created_count + skipped_count}")


if __name__ == "__main__":
    main()
