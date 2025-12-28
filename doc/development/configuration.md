# Configuration Guide

## Configuration Philosophy

Rite follows a **Single Point of Truth** principle: every tool has exactly ONE configuration file.

This eliminates:

-   ❌ Duplicate settings across multiple files
-   ❌ Conflicting configurations
-   ❌ Uncertainty about which config is used
-   ❌ Maintenance overhead

## Configuration Files

### Critical Tools

| Tool       | Config File      | Purpose                           |
| ---------- | ---------------- | --------------------------------- |
| **Poetry** | `pyproject.toml` | Package metadata and dependencies |
| **Black**  | `pyproject.toml` | Code formatting                   |
| **isort**  | `.isort.cfg`     | Import sorting                    |
| **Pytest** | `pytest.ini`     | Test framework                    |
| **Git**    | `.gitignore`     | Version control exclusions        |

### Code Quality Tools

| Tool         | Config File      | Purpose              |
| ------------ | ---------------- | -------------------- |
| **Flake8**   | `.flake8`        | PEP8 linting         |
| **Pylint**   | `.pylintrc`      | Static code analysis |
| **Mypy**     | `mypy.ini`       | Type checking        |
| **Bandit**   | `pyproject.toml` | Security scanning    |
| **Coverage** | `.coveragerc`    | Code coverage        |

### Development Tools

| Tool             | Config File               | Purpose                   |
| ---------------- | ------------------------- | ------------------------- |
| **Tox**          | `tox.ini`                 | Multi-environment testing |
| **Pre-commit**   | `.pre-commit-config.yaml` | Git hooks                 |
| **EditorConfig** | `.editorconfig`           | Editor settings           |
| **VS Code**      | `.vscode/settings.json`   | IDE configuration         |

## Common Settings

All tools are configured with consistent settings:

### Line Length

**79 characters** (Black standard)

Used by: Black, isort, Flake8, Pylint, EditorConfig, VS Code

### Python Version

**>=3.10, <4.0**

Target: Python 3.10, 3.11, 3.12

### Type Hints

**Modern Python 3.10+ syntax**

```python
# ✅ Correct
def func(x: str | None) -> list[str]:
    pass

# ❌ Incorrect (old style)
from typing import Optional, List
def func(x: Optional[str]) -> List[str]:
    pass
```

### Import Organization

Four sections in order:

1. **Future**: `from __future__ import annotations`
2. **Standard Library**: Alphabetical
3. **Libraries**: External packages (none in src/)
4. **Local Modules**: From rite package

## Tool-Specific Settings

### Black

**File:** `pyproject.toml`

```toml
[tool.black]
line-length = 88
target-version = ["py310", "py311", "py312"]
include = '\.pyi?$'
extend-exclude = '''
/(
  \.eggs
  | \.git
  | \.venv
  | build
  | dist
)/
'''
```

### isort

**File:** `.isort.cfg`

```ini
[settings]
profile = black
line_length = 79
known_first_party = rite
import_heading_future = Import | Future
import_heading_stdlib = Import | Standard Library
import_heading_thirdparty = Import | Libraries
import_heading_firstparty = Import | Local Modules
```

### Flake8

**File:** `.flake8`

```ini
[flake8]
max-line-length = 79
extend-ignore = E203, W503
max-complexity = 15
exclude = .git,__pycache__,build,dist,.venv
```

### Pylint

**File:** `.pylintrc`

```ini
[MASTER]
max-line-length = 79
disable = C0111  # missing-docstring in specific cases

[DESIGN]
max-args = 7
max-locals = 15
```

### Mypy

**File:** `mypy.ini`

```ini
[mypy]
python_version = 3.10
strict_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
```

### Pytest

**File:** `pytest.ini`

```ini
[pytest]
testpaths = tst
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow tests
```

### Coverage

**File:** `.coveragerc`

```ini
[run]
source = src/rite
branch = True

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

## Environment-Specific Settings

### Development

```bash
# .env (not in git)
RITE_ENV=development
RITE_DEBUG=true
RITE_LOG_LEVEL=DEBUG
PYTHONPATH=src
```

### Testing

```bash
# CI environment
RITE_ENV=test
CI=true
COVERAGE_FILE=.coverage
```

### Production

```bash
# Production settings
RITE_ENV=production
RITE_DEBUG=false
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
```

## IDE Configuration

### VS Code

**File:** `.vscode/settings.json`

Key settings:

-   Black as default formatter
-   Format on save enabled
-   isort on save enabled
-   Flake8, Pylint, Mypy enabled
-   Pytest as test framework
-   Line length indicators at 79

### PyCharm

1. Settings → Tools → Black
    - Enable "On code reformat"
2. Settings → Tools → isort
    - Enable "On save"
3. Settings → Editor → Code Style → Python
    - Hard wrap at 79
4. Settings → Tools → Python Integrated Tools
    - Default test runner: pytest

## Verification

Verify all tools are configured correctly:

```bash
# Run verification script
poetry run python bin/verify_tools.py

# Or manually
poetry run black --version
poetry run isort --version
poetry run flake8 --version
poetry run pylint --version
poetry run mypy --version
```

## Updating Configuration

When updating tool settings:

1. **Modify only ONE file** (single point of truth)
2. **Test the change**:
    ```bash
    make check
    ```
3. **Update documentation** if needed
4. **Commit with descriptive message**:
    ```bash
    git commit -m "config: Update Black line length"
    ```

## Configuration Matrix

For a complete overview of all settings, see the original configuration documentation in `tmp/old-docs/`.

## Best Practices

### ✅ Do

-   Keep settings consistent across tools
-   Use dedicated config files for each tool
-   Document configuration changes
-   Test configuration changes

### ❌ Don't

-   Duplicate settings in multiple files
-   Override settings locally without team agreement
-   Ignore configuration warnings
-   Mix configuration styles

## Resources

-   [Black Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
-   [isort Configuration](https://pycqa.github.io/isort/docs/configuration/config_files.html)
-   [Flake8 Configuration](https://flake8.pycqa.org/en/latest/user/configuration.html)
-   [Pylint Configuration](https://pylint.pycqa.org/en/latest/user_guide/configuration/index.html)
-   [Mypy Configuration](https://mypy.readthedocs.io/en/stable/config_file.html)
-   [Pytest Configuration](https://docs.pytest.org/en/stable/reference/customize.html)

## See Also

-   [Development Setup](setup.md)
-   [Code Style Guidelines](code-style.md)
-   [Testing Guide](testing.md)
