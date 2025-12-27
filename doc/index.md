# Rite Documentation

Welcome to the **Rite** documentation! Rite is a modern Python utility library providing a comprehensive collection of utilities for cryptography, filesystem operations, text processing, collections, conversions, and more.

## Features

- **Zero Dependencies**: No external runtime dependencies
- **Type Safe**: Comprehensive type hints with Python 3.10+ syntax
- **Well Tested**: >80% code coverage
- **Modern Python**: Python 3.10, 3.11, 3.12 support
- **Modular**: Clear module organization with consistent structure
- **Documented**: Extensive documentation and examples

## Quick Links

### Getting Started
- [Installation](installation.md) - Install Rite in your project
- [Getting Started](getting-started.md) - Quick introduction and basic usage
- [Examples](examples.md) - Practical usage examples
- [Quick Start](quick_start.md) - Jump right in

### For Contributors
- [Contributing](contributing.md) - How to contribute to Rite
- [Development Setup](development/setup.md) - Set up your development environment
- [Code Style](development/code-style.md) - Code style guidelines
- [Testing](development/testing.md) - Testing practices
- [Configuration](development/configuration.md) - Configuration reference

### For AI Agents
- [AI Instructions](development/ai-instructions.md) - Guidelines for AI agents and GitHub Copilot

### Reference
- [API Documentation](api/index.md) - Complete API reference
- [Changelog](../CHANGELOG.md) - Version history
- [Architecture](../ARCHITECTURE.txt) - System architecture

## Module Overview

### Cryptography (`rite.crypto`)
UUID generation, hashing (SHA-256, MD5, BLAKE2), HMAC, and cryptographic utilities.

### Filesystem (`rite.filesystem`)
File and directory operations, path utilities, safe file handling.

### Text Processing (`rite.text`)
Slug generation, case conversion, text sanitization, text analysis.

### Collections (`rite.collections`)
List and dictionary utilities, data structures, iteration helpers.

### Conversions (`rite.conversion`)
Type conversions, data format transformations (JSON, CSV, etc.).

### Numeric (`rite.numeric`)
Mathematical utilities, statistics, number operations.

### Temporal (`rite.temporal`)
Date and time utilities, timestamp operations, formatting.

## Requirements

- Python 3.10 or higher
- No external dependencies

## Installation

```bash
# Using pip
pip install rite

# Using Poetry
poetry add rite

# From source
git clone https://github.com/scape-agency/rite.git
cd rite
poetry install
```

## Basic Usage

```python
# Cryptography
from rite.crypto.uuid import uuid_hex
from rite.crypto.hash import hash_sha256

user_id = uuid_hex()
password_hash = hash_sha256("secure_password")

# Filesystem
from rite.filesystem.file import file_copy, file_exists

if file_exists("config.json"):
    file_copy("config.json", "config.backup.json")

# Text Processing
from rite.text.slug import slug_generate
from rite.text.case import case_to_snake

slug = slug_generate("Hello World!")  # 'hello-world'
snake = case_to_snake("helloWorld")  # 'hello_world'

# Collections
from rite.collections.list import list_unique, list_flatten

unique = list_unique([1, 2, 2, 3])  # [1, 2, 3]
flat = list_flatten([[1, 2], [3, 4]])  # [1, 2, 3, 4]
```

## About Scape Agency

**rite** is an open-source project by [Scape Agency](https://www.scape.agency).

Scape Agency is a spatial innovation collective that dreams, discovers and designs the everyday of tomorrow. We blend design thinking with emerging technologies to create a brighter perspective for people and planet. Our products and services naturalise technology in liveable and sustainable –scapes that spark the imagination and inspire future generations.

- Website: [scape.agency](https://www.scape.agency)
- GitHub: [github.com/scape-agency](https://github.com/scape-agency)
