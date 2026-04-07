# Code Style Guide

This document defines the coding standards and style guidelines for Rite.

## Core Principles

1. **Consistency**: All code follows the same structure and style
2. **Modern Python**: Use Python 3.10+ features exclusively
3. **Type Safety**: Comprehensive type hints throughout
4. **Clarity**: Code should be self-documenting
5. **Simplicity**: Favor simple, readable solutions

## Python Version

### Target: Python 3.10+

**Use modern syntax:**

```python
# ✅ Correct (Python 3.10+)
from __future__ import annotations

def process(data: str | None = None) -> dict[str, Any]:
    pass

def get_items() -> list[tuple[str, int]]:
    pass

# ❌ Incorrect (Old style)
from typing import Optional, Dict, List, Tuple

def process(data: Optional[str] = None) -> Dict[str, Any]:
    pass

def get_items() -> List[Tuple[str, int]]:
    pass
```

**NO Python 2 compatibility code:**

```python
# ❌ Don't use
# -*- coding: utf-8 -*-
from __future__ import print_function
unicode_string = u"text"

# ✅ Use
from __future__ import annotations
text = "text"  # Already Unicode in Python 3
```

## File Structure

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

## Naming Conventions

### Module Files

Use module-specific prefixes based on location:

```
crypto/uuid/uuid_hex.py         # uuid_ prefix
crypto/hash/hash_sha256.py      # hash_ prefix
filesystem/file/file_copy.py    # file_ prefix
text/slug/slug_is_valid.py      # slug_ prefix
```

### Functions and Variables

```python
# ✅ snake_case
def calculate_total(items: list[float]) -> float:
    total_sum = sum(items)
    return total_sum

# ❌ camelCase (only for classes)
def calculateTotal(items: list[float]) -> float:
    totalSum = sum(items)
    return totalSum
```

### Classes

```python
# ✅ PascalCase
class UserAccount:
    pass

class HTTPRequest:
    pass

# ❌ snake_case
class user_account:
    pass
```

### Constants

```python
# ✅ UPPER_CASE
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# ❌ Other cases
maxRetries = 3
default_timeout = 30
```

### Private Members

```python
class MyClass:
    def __init__(self):
        self._private = "internal use"
        self.__really_private = "name mangled"

    def _internal_method(self):
        pass

    def public_method(self):
        pass
```

## Type Hints

### Always Provide Type Hints

```python
# ✅ Correct
def process_data(
    data: str,
    options: dict[str, Any],
    count: int = 0
) -> tuple[bool, str]:
    return True, "processed"

# ❌ Incorrect
def process_data(data, options, count=0):
    return True, "processed"
```

### Use Modern Syntax

```python
# ✅ Python 3.10+ union syntax
def get_value() -> str | None:
    pass

def process(items: list[str | int]) -> dict[str, Any]:
    pass

# ❌ Old typing module syntax
from typing import Optional, Union, Dict, Any

def get_value() -> Optional[str]:
    pass

def process(items: List[Union[str, int]]) -> Dict[str, Any]:
    pass
```

### Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar("T")

def first_or_default(items: list[T], default: T) -> T:
    """Return first item or default value."""
    return items[0] if items else default

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value
```

## Documentation

### Docstrings (Google Style)

```python
def complex_function(
    param1: str,
    param2: int = 0,
    param3: bool = True
) -> dict[str, Any]:
    """
    Brief one-line description.

    Longer description explaining the function's purpose,
    behavior, and any important details.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 0.
        param3: Description of param3. Defaults to True.

    Returns:
        Dictionary containing processed results with keys:
        - 'status': Processing status
        - 'data': Processed data

    Raises:
        ValueError: When param1 is empty.
        TypeError: When param2 is not an integer.

    Examples:
        >>> complex_function("test", 5)
        {'status': 'ok', 'data': [...]}

        >>> complex_function("")
        Traceback (most recent call last):
        ValueError: param1 cannot be empty
    """
    if not param1:
        raise ValueError("param1 cannot be empty")

    return {"status": "ok", "data": []}
```

### Comments

```python
# Use comments sparingly - code should be self-documenting

# ✅ Good comments explain WHY
# We use binary search here because the list is pre-sorted
# and can contain millions of items
result = binary_search(items, target)

# ❌ Bad comments explain WHAT (obvious from code)
# Increment counter by 1
counter += 1
```

## Import Organization

### Four Sections (Required Order)

```python
# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import json
import os
from pathlib import Path
from typing import Any

# Import | Libraries
# (No external libraries allowed in src/)

# Import | Local Modules
from rite.crypto.hash import hash_sha256
from rite.text.slug import slug_is_valid
```

### Import Rules

```python
# ✅ Correct
import os
import sys
from pathlib import Path
from typing import Any, TypeVar

from rite.module import function

# ❌ Incorrect
import sys, os  # Don't combine imports
from pathlib import *  # Don't use star imports
from typing import Any
import os  # Wrong order
```

## Code Formatting

### Line Length: 79 Characters

```python
# ✅ Correct
def long_function_name(
    parameter_one: str,
    parameter_two: int,
    parameter_three: bool = False
) -> dict[str, Any]:
    pass

# ❌ Too long
def long_function_name(parameter_one: str, parameter_two: int, parameter_three: bool = False) -> dict[str, Any]:
    pass
```

### Whitespace

```python
# ✅ Correct spacing
def func(x: int) -> int:
    result = x + 1
    return result

items = [1, 2, 3, 4]
data = {"key": "value"}

# ❌ Incorrect spacing
def func(x:int)->int:
    result=x+1
    return result

items=[1,2,3,4]
data={"key":"value"}
```

### String Quotes

```python
# ✅ Double quotes (Black default)
text = "Hello, world!"
multiline = """
This is a
multiline string.
"""

# ✅ Single quotes for string containing double quotes
message = 'He said, "Hello!"'

# Black will normalize to double quotes where possible
```

## Error Handling

### Use Specific Exceptions

```python
# ✅ Correct
def read_file(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except PermissionError as e:
        raise ValueError(f"Cannot read {path}") from e

# ❌ Incorrect
def read_file(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except:  # Too broad
        return ""
```

### Return None for Optional Results

```python
# ✅ Correct
def find_user(user_id: int) -> User | None:
    """Find user by ID or return None if not found."""
    try:
        return get_user(user_id)
    except UserNotFound:
        return None

# ❌ Incorrect (raising for expected conditions)
def find_user(user_id: int) -> User:
    """Find user by ID."""
    # Raises exception for normal "not found" case
    return get_user(user_id)
```

## Best Practices

### Use Context Managers

```python
# ✅ Correct
with open("file.txt") as f:
    data = f.read()

# ❌ Incorrect
f = open("file.txt")
data = f.read()
f.close()
```

### Use Comprehensions

```python
# ✅ List comprehension
squares = [x**2 for x in range(10)]

# ✅ Dict comprehension
mapping = {str(i): i for i in range(10)}

# ✅ Generator expression for large data
total = sum(x**2 for x in range(1000000))

# ❌ Verbose loop
squares = []
for x in range(10):
    squares.append(x**2)
```

### Use f-strings

```python
# ✅ Correct
name = "Alice"
age = 30
message = f"{name} is {age} years old"

# ❌ Incorrect
message = "%s is %d years old" % (name, age)
message = "{} is {} years old".format(name, age)
```

### Use Pathlib

```python
from pathlib import Path

# ✅ Correct
path = Path("data") / "file.txt"
if path.exists():
    content = path.read_text()

# ❌ Incorrect
import os
path = os.path.join("data", "file.txt")
if os.path.exists(path):
    with open(path) as f:
        content = f.read()
```

## What to Avoid

### No External Dependencies in src/

```python
# ❌ Never import external libraries in src/
import requests
import numpy as np

# ✅ Use only standard library
import json
import urllib.request
```

### No Legacy Code

```python
# ❌ Don't use
print "Hello"  # Python 2 syntax
dict.iteritems()  # Python 2 method
xrange()  # Python 2 function

# ✅ Use
print("Hello")
dict.items()
range()
```

### No Commented-Out Code

```python
# ❌ Don't leave commented code
# def old_function():
#     pass

# ✅ Remove it (it's in git history if needed)
def new_function():
    pass
```

## Testing Code Style

Tests follow the same style guidelines with additions:

```python
# =============================================================================
# Test: Module Name
# =============================================================================

"""Tests for rite.module.function.
"""


# =============================================================================
# Imports
# =============================================================================

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

## Verification

Check your code follows the style guide:

```bash
# Format code
make format

# Check style
make check

# Individual tools
poetry run black src/ tst/
poetry run isort src/ tst/
poetry run flake8 src/
poetry run pylint src/
poetry run mypy src/
```

## Resources

-   [Black Code Style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
-   [PEP 8](https://peps.python.org/pep-0008/)
-   [PEP 484](https://peps.python.org/pep-0484/) - Type Hints
-   [PEP 526](https://peps.python.org/pep-0526/) - Variable Annotations
-   [PEP 604](https://peps.python.org/pep-0604/) - Union Operators
-   [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## See Also

-   [Development Setup](setup.md)
-   [Configuration Guide](configuration.md)
-   [AI Instructions](ai-instructions.md)
