# Contributing to Rite

Thank you for your interest in contributing to Rite! We welcome contributions from the community.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/scape-agency/rite/blob/main/CODE_OF_CONDUCT.md).

## Getting Started

### 1. Fork and Clone

```bash
# Fork on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/rite.git
cd rite
```

### 2. Set Up Development Environment

```bash
# Install Poetry if needed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install --install-hooks
poetry run pre-commit install --hook-type commit-msg
```

### 3. Create a Branch

```bash
git checkout -b feat/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Development Workflow

### Code Standards

Rite follows strict code quality standards:

- **Python 3.12+** syntax only
- **Zero runtime dependencies** in src/
- **Type hints** on all functions
- **Google-style docstrings**
- **79 character line length**
- **Modular file structure** with prefixes

See [AI Instructions](development/ai-instructions.md) for detailed guidelines.

### File Structure

Every module file follows this template:

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

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make coverage

# Run specific tests
poetry run pytest tst/path/to/test_file.py

# Run tests in Docker
make docker-test
```

### Code Quality Checks

```bash
# Format code
make format

# Check formatting
make format-check

# Lint code
make lint

# Type check
make type-check

# Security scan
make security

# Run all checks
make check
```

### Pre-commit Hooks

Pre-commit hooks run automatically on commit:

- File checks (trailing whitespace, EOF, merge conflicts)
- Black formatting
- isort import sorting
- Flake8 linting
- Mypy type checking
- Bandit security scanning
- pydocstyle docstring validation

To run manually:

```bash
pre-commit run --all-files
```

## Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(crypto): Add new hash function
fix(text): Fix slug validation bug
docs(readme): Update installation instructions
test(collections): Add cache tests
refactor(filesystem): Simplify file operations
style(all): Format with Black
ci(github): Update workflow
chore(deps): Update dependencies
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `perf`: Performance improvement
- `test`: Tests
- `build`: Build system
- `ci`: CI/CD
- `chore`: Maintenance

Scopes (module names):
- `crypto`, `filesystem`, `text`, `collections`, `conversion`, `numeric`, `temporal`, `core`, `tests`, `docs`, `ci`, `deps`, `config`

## Pull Request Process

### 1. Ensure Quality

- All tests pass
- Coverage maintained or improved
- No linting errors
- Type checking passes
- Documentation updated

### 2. Update Documentation

- Add docstrings to new functions
- Update relevant markdown files
- Add examples if applicable
- Update CHANGELOG.md

### 3. Submit PR

Use one of the PR templates:
- [Feature PR Template](https://github.com/scape-agency/rite/blob/main/.github/PULL_REQUEST_TEMPLATE.md)
- [Bugfix PR Template](https://github.com/scape-agency/rite/blob/main/.github/PULL_REQUEST_TEMPLATE.md)

Fill in:
- Clear description
- Motivation and context
- Testing performed
- Breaking changes (if any)
- Related issues

### 4. Review Process

- CI checks must pass
- At least one maintainer approval required
- Address review comments promptly
- Keep PR focused and small when possible

## Development Tips

### Using Make Commands

```bash
make help              # Show all commands
make dev               # Install dev dependencies
make quick             # Format and lint
make ci                # Run all CI checks
make docker-dev        # Build dev container
make hooks-install     # Install git hooks
make version           # Show current version
```

### Using VS Code

The repository includes VS Code configurations:

- `.vscode/settings.json` - IDE settings
- `.vscode/launch.json` - Debug configurations
- `.vscode/tasks.json` - Task definitions
- `.vscode/snippets.code-snippets` - Code snippets

### Using Dev Container

Open in VS Code with Dev Containers extension:

1. Install Docker and VS Code Dev Containers extension
2. Open folder in VS Code
3. Command Palette: "Dev Containers: Reopen in Container"
4. Environment is automatically set up

See the [Dev Container documentation](https://github.com/scape-agency/rite/tree/main/.devcontainer) for details.

## Adding New Modules

### 1. Choose Location

```
src/rite/
├── crypto/          # Cryptographic utilities
├── filesystem/      # File system operations
├── text/            # Text processing
├── collections/     # Collection utilities
├── conversion/      # Type conversions
├── numeric/         # Numeric utilities
└── temporal/        # Date/time utilities
```

### 2. Use Module Prefix

Files should use module-specific prefixes:

- `crypto/uuid/uuid_hex.py` (uuid_ prefix)
- `crypto/hash/hash_sha256.py` (hash_ prefix)
- `filesystem/file/file_copy.py` (file_ prefix)
- `text/slug/slug_is_valid.py` (slug_ prefix)

### 3. Create Test File

Mirror structure in `tst/`:

```
tst/
└── rite/
    └── module/
        └── test_function.py
```

### 4. Update __init__.py

Add exports to module's `__init__.py`.

### 5. Add Documentation

- Comprehensive docstrings with examples
- Update API reference if needed
- Add usage examples

## Reporting Issues

### Bug Reports

Use the [bug report template](https://github.com/scape-agency/rite/issues/new?template=bug_report.md):

- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Code sample (if applicable)

### Feature Requests

Use the [feature request template](https://github.com/scape-agency/rite/issues/new?template=feature_request.md):

- Clear description
- Use case and motivation
- Proposed API (if applicable)
- Alternatives considered

## Release Process

Releases are automated using semantic-release:

1. Merge to `main` branch
2. Semantic-release analyzes commits
3. Version bumped automatically
4. Changelog updated
5. GitHub release created
6. Published to PyPI

## Community

- **GitHub Discussions**: Ask questions, share ideas
- **GitHub Issues**: Report bugs, request features
- **Pull Requests**: Contribute code

## Recognition

Contributors are recognized in:
- [AUTHORS.md](about/authors.md)
- GitHub contributors page
- Release notes

## Questions?

- Check existing documentation
- Search GitHub issues
- Ask in GitHub Discussions
- Contact maintainers

Thank you for contributing to Rite! 🎉
