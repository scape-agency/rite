# Installation Guide

## Requirements

-   **Python**: >=3.12, <4.0
-   **Operating System**: Linux, macOS, Windows
-   **Package Manager**: pip or Poetry (recommended)

## Installation Methods

### Using pip (Recommended for Users)

```bash
# Install latest version
pip install rite

# Install specific version
pip install "rite==<version>"

# Upgrade to latest version
pip install --upgrade rite
```

### Using Poetry (Recommended for Development)

```bash
# Add to project
poetry add rite

# Add specific version
poetry add "rite@<version>"

# Add with development dependencies
poetry add rite --group dev
```

### From Source

```bash
# Clone the repository
git clone https://github.com/scape-agency/rite.git
cd rite

# Install with Poetry
poetry install

# Or install with pip
pip install -e .
```

## Verify Installation

```python
import rite

print(rite.__version__)
```

Or from command line:

```bash
python -c "import rite; print(rite.__version__)"
```

## Virtual Environment

It's recommended to use a virtual environment:

### Using venv

```bash
# Create virtual environment
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\\Scripts\\activate

# Install rite
pip install rite
```

### Using Poetry

Poetry automatically creates and manages virtual environments:

```bash
poetry install
poetry shell
```

## Docker

Use the provided Dev Container for a complete development environment:

```bash
# Open in VS Code with Dev Containers extension
# Or build manually
cd .devcontainer
docker-compose build
docker-compose up
```

See the [Dev Container documentation](https://github.com/scape-agency/rite/tree/main/.devcontainer) for details.

## Troubleshooting

### Python Version Issues

Ensure you have Python 3.12 or higher:

```bash
python --version
```

If you have multiple Python versions:

```bash
python3.12 -m pip install rite
```

### Permission Errors

On Linux/macOS, you might need to use `--user`:

```bash
pip install --user rite
```

Or use a virtual environment (recommended).

### Poetry Issues

If Poetry is not found:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
```

## Next Steps

-   [Quick Start Guide](getting-started.md)
-   [API Reference](api/index.md)
-   [Examples](examples.md)
