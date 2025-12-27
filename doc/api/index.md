---
title: API Reference
description: Complete API documentation for Rite Python library. Browse 13 modules including text processing, cryptography, filesystem, temporal, and more.
keywords: python api, rite api, python documentation, text processing api, crypto api, filesystem api
---

# API Reference

Welcome to the Rite API reference documentation. This section provides detailed documentation for all modules, classes, and functions in the Rite library.

## Module Overview

Rite is organized into semantic submodules, each focusing on a specific domain:

### Core Utilities

- **[Collections](collections.md)** - Advanced data structures and collection utilities
- **[Conversion](conversion.md)** - Type conversion and format transformation utilities
- **[Text](text.md)** - Comprehensive text processing and manipulation

### System & I/O

- **[Filesystem](filesystem.md)** - File and directory operations
- **[System](system.md)** - System-level operations and environment management
- **[Net](net.md)** - Network utilities and URL handling

### Data & Serialization

- **[Serialization](serialization.md)** - JSON, CSV, TOML, Pickle, and INI operations
- **[Markup](markup.md)** - HTML, XML, and Markdown processing

### Security & Data Processing

- **[Crypto](crypto.md)** - Cryptographic operations, hashing, and UUIDs
- **[Numeric](numeric.md)** - Numerical operations and mathematical utilities
- **[Temporal](temporal.md)** - Date, time, and duration management

### Development & Debugging

- **[Diagnostics](diagnostics.md)** - Logging, profiling, and error handling
- **[Functional](functional.md)** - Functional programming utilities
- **[Reflection](reflection.md)** - Runtime introspection and dynamic loading

## Quick Start

```python
from rite.text import to_snake_case, slugify
from rite.filesystem import file_read_text, file_write_text
from rite.crypto import hash_sha256
from rite.temporal import datetime_now

# Text processing
snake = to_snake_case("HelloWorld")  # "hello_world"
slug = slugify("Hello World!")  # "hello-world"

# File operations
content = file_read_text("example.txt")
file_write_text("output.txt", content)

# Cryptography
hashed = hash_sha256("secret data")

# Date/time
now = datetime_now()
```

## Design Principles

1. **Zero External Dependencies** - Uses only Python standard library
2. **Single Symbol Files** - Each file contains one function/class for clarity
3. **Semantic Organization** - Intuitive directory structure
4. **Complete Type Hints** - Full Python 3.10+ type annotations
5. **Comprehensive Docstrings** - Google-style documentation with examples
6. **79-Character Lines** - PEP 8 compliant formatting

## Navigation

Browse the API documentation by selecting a module from the navigation menu or use the links above to explore specific functionality.
