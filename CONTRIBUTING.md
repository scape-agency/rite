# Contributing to rite

Thank you for your interest in contributing to **rite**! We welcome contributions from the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your feature or bugfix
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.10 or higher
- Poetry for dependency management
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/rite.git
cd rite

# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Install Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

```bash
poetry run pre-commit install
```

This will run code formatters and linters before each commit.

## Making Changes

1. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** following our [code style guidelines](#code-style)

3. **Write tests** for your changes (see [Testing](#testing))

4. **Update documentation** if necessary

## Testing

We use pytest for testing. All tests should be placed in the `tst/` directory.

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=rite --cov-report=term-missing

# Run specific test file
poetry run pytest tst/time/test_timestamp.py

# Run tests matching a pattern
poetry run pytest -k "test_timestamp"
```

### Writing Tests

- Place tests in appropriate subdirectories under `tst/`
- Name test files with `test_` prefix (e.g., `test_feature.py`)
- Name test functions with `test_` prefix (e.g., `test_function_behavior()`)
- Use descriptive test names
- Include docstrings explaining what the test validates
- Use pytest fixtures for common setup

Example:

```python
import pytest
from rite.time.timestamp import get_timestamp

def test_timestamp_returns_integer():
    """Test that get_timestamp returns an integer value."""
    result = get_timestamp()
    assert isinstance(result, int)
```

## Code Style

We follow PEP 8 style guidelines with some modifications:

- **Line length**: 88 characters (Black default)
- **Import sorting**: Use isort with Black profile
- **Type hints**: Add type hints where possible
- **Docstrings**: Use Google-style docstrings

### Formatting Tools

The following tools are run automatically via pre-commit hooks:

- **Black**: Code formatter
- **isort**: Import sorter
- **flake8**: Linter
- **mypy**: Type checker

### Manual Formatting

```bash
# Format code with Black
poetry run black src/

# Sort imports
poetry run isort src/

# Run linter
poetry run flake8 src/

# Type check
poetry run mypy src/rite
```

## Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

   Write clear, concise commit messages following conventional commits:
   - `feat: Add new feature`
   - `fix: Fix bug in module`
   - `docs: Update documentation`
   - `test: Add tests`
   - `refactor: Refactor code`
   - `style: Format code`
   - `chore: Update dependencies`

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template with:
     - Description of changes
     - Related issue numbers (if any)
     - Screenshots (if applicable)
     - Testing steps

4. **Wait for review**:
   - Address any feedback from reviewers
   - Make requested changes
   - Push updates to your branch (PR will update automatically)

## Pull Request Guidelines

- **One feature per PR**: Keep PRs focused on a single feature or fix
- **Update tests**: Add or update tests for your changes
- **Update docs**: Update documentation if you change functionality
- **Pass CI checks**: Ensure all CI checks pass
- **Keep commits clean**: Squash commits if necessary
- **Follow style guide**: Ensure code follows our style guidelines

## Questions?

If you have questions or need help:

- Open an issue with the `question` label
- Start a discussion in GitHub Discussions
- Contact the maintainers at info@scape.agency

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
