#!/bin/bash

# =============================================================================
# Post-Create Script for Rite Dev Container
# =============================================================================
# This script runs after the dev container is created

set -e

echo "🚀 Setting up Rite development environment..."

# Update pip
echo "📦 Updating pip..."
python -m pip install --upgrade pip

# Install dependencies with Poetry
if [ -f "pyproject.toml" ]; then
    echo "📦 Installing project dependencies..."
    poetry install --no-interaction --with dev
    echo "✅ Dependencies installed"
else
    echo "⚠️  No pyproject.toml found, skipping dependency installation"
fi

# Install pre-commit hooks
if [ -f ".pre-commit-config.yaml" ]; then
    echo "🪝 Installing pre-commit hooks..."
    poetry run pre-commit install --install-hooks
    poetry run pre-commit install --hook-type commit-msg
    echo "✅ Pre-commit hooks installed"
fi

# Set up git configuration
echo "🔧 Configuring git..."
git config --global core.autocrlf input
git config --global core.eol lf
git config --global init.defaultBranch main
git config --global pull.rebase false

# Verify tools
echo "🔍 Verifying development tools..."
echo "Python: $(python --version)"
echo "Poetry: $(poetry --version)"
echo "Git: $(git --version)"

# Show installed Python packages
echo "📋 Installed Python packages:"
poetry show --tree

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p .pytest_cache
mkdir -p htmlcov
mkdir -p doc/_build

# Set permissions
echo "🔐 Setting permissions..."
chmod -R 755 .

echo "✅ Development environment setup complete!"
echo ""
echo "🎉 Ready to develop!"
echo ""
echo "Quick commands:"
echo "  make help           - Show all available commands"
echo "  make dev            - Install dev dependencies"
echo "  make test           - Run tests"
echo "  make format         - Format code"
echo "  make check          - Run all checks"
echo ""
