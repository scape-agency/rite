# Development Setup Guide

This guide will help you set up your development environment for Rite.

## Prerequisites

- **Python**: 3.10, 3.11, or 3.12
- **Git**: For version control
- **Poetry**: 1.8.0 or higher (recommended)
- **Docker**: Optional, for Dev Container

## Initial Setup

### 1. Clone Repository

```bash
git clone https://github.com/scape-agency/rite.git
cd rite
```

### 2. Install Poetry

If you don't have Poetry installed:

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Verify installation
poetry --version
```

### 3. Install Dependencies

```bash
# Install all dependencies including dev tools
poetry install --with dev

# Verify installation
poetry run python -c "import rite; print(rite.__version__)"
```

### 4. Set Up Pre-commit Hooks

```bash
# Install pre-commit hooks
poetry run pre-commit install --install-hooks
poetry run pre-commit install --hook-type commit-msg

# Test hooks
poetry run pre-commit run --all-files
```

## Development Tools

All development tools are pre-configured:

### Code Formatting

- **Black**: Code formatter (79 char line length)
- **isort**: Import sorter (Black-compatible)

```bash
# Format code
make format

# Check formatting
make format-check
```

### Linting

- **Flake8**: PEP8 linting
- **Pylint**: Static code analysis

```bash
# Lint code
make lint

# Or individually
poetry run flake8 src/
poetry run pylint src/
```

### Type Checking

- **Mypy**: Static type checker

```bash
# Type check
make type-check

# Or directly
poetry run mypy src/
```

### Security

- **Bandit**: Security vulnerability scanner

```bash
# Security scan
make security

# Or directly
poetry run bandit -r src/ -c pyproject.toml
```

### Testing

- **Pytest**: Test framework
- **Coverage**: Code coverage measurement

```bash
# Run tests
make test

# Run with coverage
make coverage

# Run specific test
poetry run pytest tst/path/to/test.py

# Run with markers
poetry run pytest -m unit
poetry run pytest -m integration
```

## Configuration Files

All tools have dedicated configuration files:

| Tool | Config File | Location |
|------|-------------|----------|
| Black | `pyproject.toml` | `[tool.black]` |
| isort | `.isort.cfg` | Root |
| Flake8 | `.flake8` | Root |
| Pylint | `.pylintrc` | Root |
| Mypy | `mypy.ini` | Root |
| Pytest | `pytest.ini` | Root |
| Coverage | `.coveragerc` | Root |
| Tox | `tox.ini` | Root |
| Pre-commit | `.pre-commit-config.yaml` | Root |
| EditorConfig | `.editorconfig` | Root |

See [Configuration Philosophy](configuration.md) for details.

## IDE Setup

### VS Code (Recommended)

The repository includes comprehensive VS Code settings:

```bash
# Open in VS Code
code .
```

Recommended extensions are automatically suggested:
- Python
- Pylance
- Black Formatter
- isort
- Flake8
- Pylint
- GitHub Copilot
- GitLens
- Coverage Gutters

Settings are pre-configured in:
- `.vscode/settings.json` - IDE settings
- `.vscode/launch.json` - Debug configurations
- `.vscode/tasks.json` - Task definitions
- `.vscode/snippets.code-snippets` - Code snippets

### Dev Container

For a complete, containerized development environment:

1. Install Docker Desktop
2. Install VS Code Dev Containers extension
3. Open Command Palette: "Dev Containers: Reopen in Container"
4. Wait for container to build (first time only)

See [.devcontainer/README.md](../../.devcontainer/README.md) for details.

## Makefile Commands

All common tasks are available via Make:

```bash
# Show all commands
make help

# Development
make dev              # Install dev dependencies
make verify           # Verify tool installation

# Code Quality
make format           # Format code
make format-check     # Check formatting
make lint             # Lint code
make type-check       # Type check
make security         # Security scan
make check            # Run all checks

# Testing
make test             # Run tests
make coverage         # Run with coverage
make tox              # Test multiple environments

# Other
make clean            # Clean build artifacts
make quick            # Format and lint
make ci               # Run all CI checks
make docs             # Build documentation
make hooks-install    # Install git hooks
make version          # Show version
make docker-build     # Build Docker image
```

## Verification

Verify your setup is correct:

```bash
# Run automated verification
poetry run python bin/verify_tools.py

# Or manually check each tool
poetry run black --version
poetry run isort --version
poetry run flake8 --version
poetry run pylint --version
poetry run mypy --version
poetry run pytest --version
poetry run coverage --version
```

## Environment Variables

Create a `.env` file (optional):

```bash
# Copy example
cp .env.example .env

# Edit as needed
PYTHONPATH=src
RITE_ENV=development
RITE_DEBUG=true
```

## Troubleshooting

### Poetry Installation Issues

```bash
# Clear cache
poetry cache clear pypi --all

# Reinstall
poetry install --with dev --no-cache
```

### Python Version Issues

```bash
# Show Poetry's Python
poetry env info

# Use specific Python
poetry env use python3.10
poetry env use python3.11
poetry env use python3.12

# Remove and recreate
poetry env remove python
poetry install --with dev
```

### Pre-commit Hook Issues

```bash
# Reinstall hooks
poetry run pre-commit uninstall
poetry run pre-commit install --install-hooks

# Update hooks
poetry run pre-commit autoupdate

# Clean and reinstall
poetry run pre-commit clean
poetry run pre-commit install --install-hooks
```

### Permission Issues

On Linux/macOS:

```bash
# Fix permissions
chmod +x bin/*.sh
chmod +x bin/*.py
```

## Workflows

### Daily Development

```bash
# 1. Pull latest changes
git pull origin dev

# 2. Create feature branch
git checkout -b feat/my-feature

# 3. Make changes and test
make quick          # Format and lint
make test           # Run tests

# 4. Commit (pre-commit runs automatically)
git add .
git commit -m "feat(module): Add new feature"

# 5. Push and create PR
git push origin feat/my-feature
```

### Before Committing

```bash
# Run all checks
make check

# Or individually
make format        # Format code
make lint          # Lint
make type-check    # Type check
make security      # Security scan
make test          # Tests
```

### Multi-Environment Testing

```bash
# Test on all Python versions
make tox

# Test specific environment
poetry run tox -e py310
poetry run tox -e py311
poetry run tox -e py312
```

## Next Steps

- Read [Contributing Guide](../contributing.md)
- Review [Code Style Guidelines](code-style.md)
- Check [AI Instructions](ai-instructions.md)
- Explore [API Reference](../api/index.md)

## Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Mypy Documentation](https://mypy.readthedocs.io/)
