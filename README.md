<header>
<p align="center">
    <img src="res/logo/rite_logo.png" width="20%" height="20%" alt="rite Logo">
</p>

<h3 align='center'>Python Utility Package</h3>
<p align="center">rites to write py right</p>

</header>

<br/>

<div align="center">
  <a href="https://github.com/scape-agency/rite/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Abug-suspected&template=bug_report.yml">Report a Bug</a>
  |
  <a href="https://github.com/scape-agency/rite/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Afeature-request%2CHelp+wanted+%F0%9F%AA%A7&template=feature_request.yml">Request a Feature</a>
  |
  <a href="https://github.com/scape-agency/rite/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Aquestion&template=question.yml">Ask a Question</a>
  |
  <a href="https://github.com/scape-agency/rite/issues/new?assignees=&labels=Needs%3A+Triage+%3Amag%3A%2Ctype%3Aenhancement&template=suggestion.yml">Make a Sugestion</a>
  |
  <a href="https://github.com/scape-agency/rite/discussions">Start a Discussion</a>
</div>

<br/>

<div align="center">

[![license](https://img.shields.io/github/license/scape-agency/rite?color=green&label=license&style=flat-square)](LICENSE.txt)
[![website](https://img.shields.io/website?color=blue&down_color=red&down_message=offline&label=website&style=flat-square&up_color=green&up_message=online&url=https%3A%2F%2Fwww.pyrites.dev)](https://www.pyrites.dev)
![python](https://img.shields.io/pypi/pyversions/rite?color=blue&label=python&style=flat-square)
![wheel](https://img.shields.io/pypi/wheel/rite?color=green&label=wheel&style=flat-square)

![stars](https://img.shields.io/github/stars/scape-agency/rite?color=blue&label=stars&style=flat-square)
![forks](https://img.shields.io/github/forks/scape-agency/rite?color=blue&label=forks&style=flat-square)
![downloads](https://img.shields.io/github/downloads/scape-agency/rite/total?color=blue&label=downloads&style=flat-square)
![issues](https://img.shields.io/github/issues/scape-agency/rite?label=issues&style=flat-square)
![sponsors](https://img.shields.io/github/sponsors/scape-agency?color=blue&label=sponsors&style=flat-square)
![contributors](https://img.shields.io/github/contributors/scape-agency/rite?color=blue&label=contributors&style=flat-square)

</div>

---

<br/>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

</details>

## About

**rite** is a comprehensive Python utility package providing a collection of reusable functions and utilities for common programming tasks. The package follows a stdlib-mirroring architecture for intuitive module organization.

### Features

**Core Modules (Zero Dependencies):**

- **text**: String processing, case conversion, slug generation, text analysis, Morse code
- **numeric**: Mathematical operations, clamping, coordinate conversions, decimal handling
- **temporal**: Timestamp handling, duration calculations, timezone utilities
- **filesystem**: Path operations and file system utilities
- **collections**: Data structures (circular buffers, singleton, nested sets)
- **serialization**: JSON, CSV, INI format handling (stdlib only)
- **conversion**: Type conversions (bool, number, percentage, decimal)
- **crypto**: Hashing and simple ciphers (stdlib only)
- **net**: HTTP and SQLite server utilities
- **markup**: HTML cleaning and manipulation
- **system**: Command execution and system operations
- **diagnostics**: Logging and error handling
- **functional**: Functional programming utilities (decorators, etc.)
- **identity**: UUID generation and validation
- **reflection**: Dynamic class loading and introspection

## Quick Start

### Installation

Install from PyPI:

```sh
pip install rite
```

Or install a specific version:

```sh
pip install rite==0.0.13
```

For development installation:

```sh
git clone https://github.com/scape-agency/rite.git
cd rite
poetry install
```

[PyPi Package](https://pypi.org/project/rite/)

## Usage

### Text Processing

```python
from rite.text import to_snake_case, to_camel_case, slugify
from rite.text import char_frequency, word_count, is_palindrome

# Case conversions
snake = to_snake_case("HelloWorld")  # "hello_world"
camel = to_camel_case("hello_world")  # "helloWorld"

# Create URL-friendly slugs
slug = slugify("Hello World!")  # "hello-world"

# Text analysis
freq = char_frequency("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
words = word_count("Hello world")  # 2
palindrome = is_palindrome("racecar")  # True
```

### Numeric Operations

```python
from rite.numeric import clamp, float_to_degree_minute_second

# Clamp values between bounds
value = clamp(15, 0, 10)  # 10

# Convert coordinates
dms = float_to_degree_minute_second(12.5)  # (12, 30, 0.0)
```

### Temporal Operations

```python
from rite.temporal import Timestamp, Duration, Timezone

# Create and manipulate timestamps
ts = Timestamp()
unix_time = ts.to_unix()

# Handle durations
duration = Duration(seconds=3661)
print(duration)  # "1h 1m 1s"

# Work with timezones
tz = Timezone("Europe/Amsterdam")
now = tz.now()
```

### Type Conversions

```python
from rite.conversion import to_bool, to_number, to_percentage

# Flexible boolean conversion
to_bool("yes")  # True
to_bool("no")   # False

# Parse numbers from strings
to_number("45.5 kg")  # 45.5

# Convert to percentage
to_percentage(0.35)  # 35.0
```

### UUID Generation

```python
from rite.identity import uuid_string, uuid_hex, is_valid_uuid

# Generate UUIDs
uuid_str = uuid_string()  # "550e8400-e29b-41d4-a716-446655440000"
uuid_compact = uuid_hex()  # "550e8400e29b41d4a716446655440000"

# Validate UUIDs
valid = is_valid_uuid("550e8400-e29b-41d4-a716-446655440000")  # True
```

### File System Operations

```python
from rite.filesystem import path_leaf

# Get the final component of a path
filename = path_leaf("/path/to/file.txt")  # "file.txt"
```

### Collections & Data Structures

```python
from rite.collections import CircularBuffer, SingletonMeta

# Use a circular buffer
buffer = CircularBuffer(size=5)
buffer.append(1)
buffer.append(2)

# Create singleton classes
class MyConfig(metaclass=SingletonMeta):
    pass
```

For more examples and documentation, visit our [documentation](https://www.pyrites.dev).

## Authors

**rite** is an open-source project by **[Scape Agency](https://www.scape.agency "Scape Agency website")**.

Scape Agency is a spatial innovation collective that dreams, discovers and designs the everyday of tomorrow. We blend design thinking with emerging technologies to create a brighter perspective for people and planet. Our products and services naturalise technology in liveable and sustainable –scapes that spark the imagination and inspire future generations.

- website: [scape.agency](https://www.scape.agency "Scape Agency website")
- github: [github.com/scape-agency](https://github.com/scape-agency "Scape Agency Github")

## License

Except where otherwise noted, **rite** is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT "MIT License").

## Contributing

We'd love for you to contribute and to make **rite** even better than it is today!
Please refer to the [contribution guidelines](CONTRIBUTING.md) for information.

## Disclaimer

**THIS SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
