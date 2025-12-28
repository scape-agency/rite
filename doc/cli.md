# Rite CLI

Command-line interface for the Rite utility library.

## Installation

After installing the package:

```bash
pip install rite
```

The `rite` command will be available:

```bash
rite --help
```

## Usage

### Version Information

```bash
rite --version
```

### Package Information

```bash
rite info
```

### Hash Text

Hash text using SHA-256 (default) or MD5:

```bash
# SHA-256 (default)
rite hash "Hello World"

# MD5
rite hash "Hello World" --algorithm md5
```

### Generate UUIDs

```bash
# Generate single UUID
rite uuid

# Generate multiple UUIDs
rite uuid --count 5

# Generate UUID in hex format
rite uuid --hex
```

### Generate URL Slugs

```bash
rite slug "Hello World! This is a Test 123"
# Output: hello-world-this-is-a-test-123
```

### Convert Text Case

```bash
# Snake case
rite case "HelloWorld" --type snake
# Output: hello_world

# Camel case
rite case "hello_world" --type camel
# Output: helloWorld

# Pascal case
rite case "hello_world" --type pascal
# Output: HelloWorld

# Kebab case
rite case "helloWorld" --type kebab
# Output: hello-world
```

### Hash File Contents

```bash
# SHA-256 (default)
rite file-hash config.json

# MD5
rite file-hash config.json --algorithm md5
```

## Command Reference

### `rite info`

Display package information and available modules.

**Options:**
- None

**Example:**
```bash
rite info
```

### `rite hash <text>`

Hash text using cryptographic algorithms.

**Arguments:**
- `text` - Text to hash

**Options:**
- `-a, --algorithm {sha256,md5}` - Hash algorithm (default: sha256)

**Example:**
```bash
rite hash "sensitive data" --algorithm sha256
```

### `rite uuid`

Generate UUIDs.

**Options:**
- `-n, --count <number>` - Number of UUIDs to generate (default: 1)
- `--hex` - Output in hex format

**Examples:**
```bash
rite uuid
rite uuid --count 10
rite uuid --hex
```

### `rite slug <text>`

Generate URL-friendly slugs.

**Arguments:**
- `text` - Text to slugify

**Example:**
```bash
rite slug "Product Name (2024)"
# Output: product-name-2024
```

### `rite case <text>`

Convert text between different case formats.

**Arguments:**
- `text` - Text to convert

**Options:**
- `-t, --type {snake,camel,pascal,kebab}` - Target case type (required)

**Examples:**
```bash
rite case "myVariableName" --type snake
# Output: my_variable_name

rite case "my-css-class" --type camel
# Output: myCssClass
```

### `rite file-hash <file>`

Hash file contents.

**Arguments:**
- `file` - File to hash

**Options:**
- `-a, --algorithm {sha256,md5}` - Hash algorithm (default: sha256)

**Example:**
```bash
rite file-hash package.json
# Output: 5d41402abc4b2a76b9719d911017c592  package.json
```

## Python API

You can also use the CLI functions programmatically:

```python
from rite.cli import cli_main
import sys

# Programmatic usage
sys.argv = ["rite", "hash", "test"]
exit_code = cli_main()
```

## Development

Run the CLI in development mode:

```bash
# Using poetry
poetry run python -m rite info

# Direct Python
python -m rite info
```

## Error Handling

The CLI returns:
- `0` - Success
- `1` - Error (with message printed to stderr)

Example error:

```bash
rite hash --algorithm invalid "text"
# Error: Unknown algorithm 'invalid'
# Exit code: 1
```

## Future Commands

Planned additions:
- `rite encode/decode` - Base64, URL encoding
- `rite json` - JSON validation and formatting
- `rite yaml` - YAML operations
- `rite template` - File templating
- `rite convert` - Unit conversions

## Contributing

To add new CLI commands:

1. Add command function in `src/rite/cli.py`
2. Register parser in `create_parser()`
3. Add documentation to this file
4. Add tests in `tst/cases/test_cli.py`
