# Getting Started with Rite

Rite is a modern Python utility library targeting Python 3.10+ with zero external runtime dependencies. This guide will help you get started quickly.

## Quick Installation

### Using pip

```bash
pip install rite
```

### Using Poetry

```bash
poetry add rite
```

## Basic Usage

```python
from rite.text.slug import slug_is_valid
from rite.crypto.hash import hash_sha256
from rite.filesystem.file import file_copy

# Validate a slug
is_valid = slug_is_valid("my-awesome-slug")  # True

# Hash a string
hashed = hash_sha256("secret")

# Copy a file
file_copy("source.txt", "destination.txt")
```

## Module Overview

Rite is organized into functional modules:

### Cryptography (`rite.crypto`)
- **uuid**: UUID generation and validation
- **hash**: Hashing functions (SHA256, MD5, etc.)
- **cipher**: Encryption and decryption utilities

### Filesystem (`rite.filesystem`)
- **file**: File operations (copy, move, read, write)
- **folder**: Directory operations
- **path**: Path manipulation utilities

### Text Processing (`rite.text`)
- **slug**: URL-friendly slug generation and validation
- **case**: Case conversion (camelCase, snake_case, etc.)
- **sanitize**: Text sanitization and cleaning
- **random**: Random string generation

### Collections (`rite.collections`)
- **buffer**: Circular buffers, ring buffers
- **cache**: LRU, LFU, TTL caches
- **queue**: Priority queues, deques
- **tree**: Tree data structures

### Conversion (`rite.conversion`)
- Type conversion utilities
- Data format conversions

### Numeric (`rite.numeric`)
- Mathematical utilities
- Number formatting and parsing

### Temporal (`rite.temporal`)
- Date and time utilities
- Timezone handling

## Next Steps

- [Installation Guide](installation.md)
- [API Reference](api/index.md)
- [Examples](examples.md)
- [Development Guide](development/setup.md)

## Requirements

- Python >=3.10, <4.0
- No external runtime dependencies

## Support

- [Documentation](https://rite.scape.agency)
- [GitHub Issues](https://github.com/scape-agency/rite/issues)
- [Contributing Guidelines](contributing.md)

## License

Rite is released under the MIT License. See [LICENSE](legal/license.md) for details.
