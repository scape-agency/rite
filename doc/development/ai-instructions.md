# AI Instructions for Rite

This guide provides comprehensive instructions for AI agents and GitHub Copilot when working on the Rite project.

## Project Overview

**Rite** is a modern Python utility library with:

-   **Target**: Python 3.10, 3.11, 3.12
-   **Dependencies**: Zero external runtime dependencies
-   **License**: MIT
-   **Repository**: https://github.com/scape-agency/rite

## Core Principles

1. **Consistency**: All code follows the same structure
2. **Modern Python**: Python 3.10+ syntax only
3. **Type Safety**: Comprehensive type hints
4. **Zero Dependencies**: No external packages in src/
5. **Modularity**: Clear module organization with prefixes

## File Structure Template

Every Python file MUST follow this exact structure:

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
│   ├── case/       # Case conversion (case_* files)
│   └── sanitize/   # Text sanitization (sanitize_* files)
├── collections/    # Collection utilities
├── conversion/     # Type conversions
├── numeric/        # Numeric utilities
└── temporal/       # Date/time utilities
```

## Naming Conventions

### Module Files

Use module-specific prefixes:

-   `crypto/uuid/uuid_hex.py`
-   `crypto/hash/hash_sha256.py`
-   `filesystem/file/file_copy.py`
-   `text/slug/slug_is_valid.py`

### Code Elements

-   **Functions/Variables**: `snake_case`
-   **Classes**: `PascalCase`
-   **Constants**: `UPPER_CASE`
-   **Private**: `_leading_underscore`

## Type Hints

Always use Python 3.10+ type hint syntax:

```python
# ✅ Correct (Python 3.10+)
def process(data: str | None = None) -> dict[str, Any]:
    pass

def get_items() -> list[tuple[str, int]]:
    pass

# ❌ Incorrect (Old style)
def process(data: Optional[str] = None) -> Dict[str, Any]:
    pass
```

## Import Organization

Four sections in exact order:

1. **Future**: `from __future__ import annotations`
2. **Standard Library**: Alphabetical
3. **Libraries**: External packages (none in src/)
4. **Local Modules**: From rite package

Use custom headers:

```python
# Import | Future
# Import | Standard Library
# Import | Libraries
# Import | Local Modules
```

## Documentation

Use Google-style docstrings:

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
    def test_multiple_cases(
        self, input_val: str, expected: str
    ) -> None:
        """Test multiple parameter combinations."""
        assert function(input_val) == expected
```

### Test Markers

-   `@pytest.mark.unit` - Unit tests
-   `@pytest.mark.integration` - Integration tests
-   `@pytest.mark.slow` - Slow tests
-   `@pytest.mark.security` - Security tests

## Code Quality Standards

### Formatting

-   **Black**: 79 character line length
-   **isort**: Black-compatible profile
-   **No trailing whitespace**
-   **LF line endings**
-   **Final newline in every file**

### Linting

-   **Flake8**: Max line length 79, max complexity 15
-   **Pylint**: Score target 10.0
-   **No unused imports**
-   **No commented-out code**

### Type Checking

-   **Mypy**: Strict optional, warn on redundant casts
-   **All functions**: Return type hints required
-   **All parameters**: Type hints required

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

## Common Commands

```bash
# Format code
make format

# Check quality
make check

# Run tests
make test

# All at once
make all
```

## Configuration Files

All tools have dedicated configuration files:

-   **Black**: `pyproject.toml` [tool.black]
-   **isort**: `.isort.cfg`
-   **Flake8**: `.flake8`
-   **Pylint**: `.pylintrc`
-   **Mypy**: `mypy.ini`
-   **Pytest**: `pytest.ini`
-   **Coverage**: `.coveragerc`

## Common Patterns

### Error Handling

```python
def safe_operation(value: str) -> str | None:
    """Return result or None on failure."""
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

## What NOT to Do

### ❌ Never Use:

-   Python 2 compatibility code
-   `# -*- coding: utf-8 -*-` declarations
-   External dependencies in src/
-   `Optional[X]` instead of `X | None`
-   `Union[X, Y]` instead of `X | Y`
-   `Dict`, `List`, `Tuple` from typing module
-   Commented-out code
-   TODO comments without issues

### ❌ Never Import:

```python
# Don't use in src/
import requests
import numpy
import pandas
```

### ✅ Only Use:

```python
# Standard library only in src/
import os
import json
from pathlib import Path
from typing import Any, TypeVar
```

## Remember

-   **Modern Python only** (3.10+)
-   **Zero runtime dependencies**
-   **Consistent structure everywhere**
-   **Type hints always**
-   **Test everything**
-   **Document thoroughly**

When in doubt, look at existing files in the codebase as examples.

## See Also

-   [Code Style Guide](code-style.md)
-   [Development Setup](setup.md)
-   [Testing Guide](testing.md)
-   [Configuration Guide](configuration.md)
-   [Contributing Guide](https://github.com/scape-agency/rite/blob/main/CONTRIBUTING.md)
