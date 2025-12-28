# GitHub Copilot Instructions for Rite Project

## Project Context

**Rite** is a modern Python utility library targeting Python 3.12+ with zero external runtime dependencies. It provides utilities for cryptography, filesystem operations, text processing, collections, conversions, and more.

## Core Principles

### 1. Python Version & Compatibility

-   **Target:** Python 3.12+
-   **Use modern syntax:** `X | None` instead of `Optional[X]`, `X | Y` instead of `Union[X, Y]`
-   **NO Python 2 compatibility code**
-   **NO coding declarations** (`# -*- coding: utf-8 -*-`)
-   **Always use:** `from __future__ import annotations`

### 2. Dependencies

-   **Runtime:** ZERO external dependencies in `src/`
-   **Use only:** Python standard library
-   **Dev dependencies:** Only in `[tool.poetry.group.dev.dependencies]`

### 3. Code Structure

Every Python file MUST follow this exact template:

```python
# =============================================================================
# Docstring
# =============================================================================

"""
Module Name
===========

Brief description.

Examples
--------
>>> from rite.module import function
>>> function(arg)
'result'
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import os
from typing import Any

# Import | Libraries
# (No external libraries in src/)

# Import | Local Modules
from rite.other_module import helper

# =============================================================================
# Functions/Classes
# =============================================================================

def function_name(param: str) -> str:
    """
    Brief description.

    Args:
        param: Parameter description.

    Returns:
        Return value description.

    Examples:
        >>> function_name("test")
        'result'
    """
    return result

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = ["function_name"]
```

### 4. Naming Conventions

**Module Files:**

-   Use module-specific prefixes based on location
-   Examples:
    -   `crypto/uuid/uuid_hex.py` (uuid\_ prefix)
    -   `crypto/hash/hash_sha256.py` (hash\_ prefix)
    -   `filesystem/file/file_copy.py` (file\_ prefix)
    -   `text/slug/slug_is_valid.py` (slug\_ prefix)

**Functions/Variables:** `snake_case`
**Classes:** `PascalCase`
**Constants:** `UPPER_CASE`
**Private:** `_leading_underscore`

### 5. Type Hints

**ALWAYS provide type hints:**

```python
# ✅ Correct (Python 3.12+)
def process(data: str | None = None) -> dict[str, Any]:
    pass

def get_items() -> list[tuple[str, int]]:
    pass

# ❌ Incorrect (Old style)
def process(data: Optional[str] = None) -> Dict[str, Any]:
    pass
```

### 6. Docstrings

**Use Google style:**

```python
def function(param1: str, param2: int = 0) -> bool:
    """
    Brief one-line description.

    Longer description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 0.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param1 is empty.

    Examples:
        >>> function("test", 5)
        True
    """
```

### 7. Import Organization

**Four sections, in order:**

1. **Future:** `from __future__ import annotations`
2. **Standard Library:** Alphabetical
3. **Libraries:** External packages (none in src/)
4. **Local Modules:** From rite package

Use custom headers:

-   `# Import | Future`
-   `# Import | Standard Library`
-   `# Import | Libraries`
-   `# Import | Local Modules`

## Code Quality Standards

### Formatting

-   **Black:** 79 character line length
-   **isort:** Black-compatible profile
-   **No trailing whitespace**
-   **LF line endings (Unix-style)**
-   **Final newline in every file**

### Linting

-   **Flake8:** Max line length 79, max complexity 15
-   **Pylint:** Score target 10.0
-   **No unused imports**
-   **No commented-out code**

### Type Checking

-   **Mypy:** Strict optional, warn on redundant casts
-   **All functions:** Return type hints required
-   **All parameters:** Type hints required

## Common Patterns

### Error Handling

```python
def safe_operation(value: str) -> str | None:
    """
    Perform operation safely.

    Returns None on failure instead of raising.
    """
    try:
        return risky_operation(value)
    except ValueError:
        return None
```

### File Operations

```python
from pathlib import Path

def read_config(path: Path | str) -> dict[str, Any]:
    """Read configuration file."""
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    return json.loads(config_path.read_text())
```

### Type Checking

```python
from typing import TypeVar

T = TypeVar("T")

def first_or_default(items: list[T], default: T) -> T:
    """Return first item or default value."""
    return items[0] if items else default
```

## Testing

### Test Structure

```python
# =============================================================================
# Test: Module Name
# =============================================================================

"""Tests for rite.module.function."""

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.module import function


class TestFunction:
    """Tests for function."""

    def test_basic_usage(self) -> None:
        """Test basic functionality."""
        result = function("input")
        assert result == "expected"

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            ("test1", "result1"),
            ("test2", "result2"),
        ],
    )
    def test_multiple_cases(self, input_val: str, expected: str) -> None:
        """Test multiple parameter combinations."""
        assert function(input_val) == expected
```

### Test Markers

-   `@pytest.mark.unit` - Unit tests
-   `@pytest.mark.integration` - Integration tests
-   `@pytest.mark.slow` - Slow tests
-   `@pytest.mark.security` - Security tests

## Module Organization

```
src/rite/
├── crypto/          # Cryptographic utilities
│   ├── uuid/       # UUID operations (uuid_* files)
│   ├── hash/       # Hashing functions (hash_* files)
│   └── cipher/     # Cipher implementations (cipher_* files)
├── filesystem/     # File system operations
│   ├── file/       # File operations (file_* files)
│   ├── folder/     # Directory operations (folder_* files)
│   └── path/       # Path utilities (path_* files)
├── text/           # Text processing
│   ├── slug/       # Slug generation (slug_* files)
│   ├── sanitize/   # Text sanitization (sanitize_* files)
│   └── converters/ # Case converters (case_to_* files)
├── collections/    # Collection utilities
├── conversion/     # Type conversions
├── numeric/        # Numeric utilities
└── temporal/       # Date/time utilities
```

## AI Agent Guidelines

### When Creating New Files:

1. Use the correct module prefix
2. Follow the four-section template exactly
3. Add comprehensive docstrings with examples
4. Include type hints for everything
5. Add `__all__` exports
6. Create corresponding test file

### When Modifying Files:

1. Maintain the four-section structure
2. Preserve import organization
3. Update `__all__` if adding exports
4. Keep docstrings up to date
5. Don't break existing type hints

### When Writing Tests:

1. Create test file in `tst/` mirroring `src/` structure
2. Use descriptive test names
3. Include parametrized tests for multiple cases
4. Test edge cases and error conditions
5. Aim for >80% coverage

### Quality Checklist:

-   [ ] Python 3.10+ syntax used
-   [ ] `from __future__ import annotations` present
-   [ ] Four-section structure followed
-   [ ] Correct module prefix in filename
-   [ ] Type hints on all functions/methods
-   [ ] Google-style docstrings with examples
-   [ ] `__all__` defined
-   [ ] No external dependencies in src/
-   [ ] Tests created/updated
-   [ ] Line length ≤ 79 characters

## Commands to Run

### Format code:

```bash
poetry run black src/ tst/
poetry run isort src/ tst/
```

### Check quality:

```bash
poetry run flake8 src/
poetry run pylint src/
poetry run mypy src/
```

### Run tests:

```bash
poetry run pytest tst/
```

### All at once:

```bash
make -f Makefile.dev all
```

## Configuration Files

All tools have dedicated configuration files:

-   **Black:** `pyproject.toml` [tool.black]
-   **isort:** `.isort.cfg`
-   **Flake8:** `.flake8`
-   **Pylint:** `.pylintrc`
-   **Mypy:** `mypy.ini`
-   **Pytest:** `pytest.ini`
-   **Coverage:** `.coveragerc`

See `CONFIG_MATRIX.md` for complete configuration details.

## Documentation

For complete guidelines, see:

-   `AI_INSTRUCTIONS.md` - Comprehensive AI guidelines (22KB)
-   `CONFIG_MATRIX.md` - Configuration matrix
-   `SINGLE_POINT_OF_TRUTH.md` - Configuration philosophy

## Remember

-   **Modern Python only** (3.12+)
-   **Zero runtime dependencies**
-   **Consistent structure everywhere**
-   **Type hints always**
-   **Test everything**
-   **Document thoroughly**

When in doubt, look at existing files in the codebase as examples of the pattern to follow.
