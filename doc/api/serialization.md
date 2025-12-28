---
title: Serialization API
description: Data format helpers from rite.serialization including JSON, CSV, TOML, Pickle, and INI utilities.
keywords: python serialization, json, csv, toml, pickle, ini, rite.serialization
---

# Serialization Module

The `rite.serialization` module provides utilities for working with
various data formats including JSON, CSV, TOML, Pickle, and INI files.

## Overview

::: rite.serialization
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### JSON

Parse and generate JSON data.

::: rite.serialization.json
options:
members: - json_load - json_loads - json_dump - json_dumps - json_validate
show_source: false
heading_level: 3

### CSV

Read and write CSV files.

::: rite.serialization.csv
options:
members: - csv_read - csv_write - csv_detect_delimiter
show_source: false
heading_level: 3

### TOML

Parse TOML configuration files (Python 3.11+).

::: rite.serialization.toml
options:
members: - toml_load - toml_loads
show_source: false
heading_level: 3

### Pickle

Serialize and deserialize Python objects.

::: rite.serialization.pickle
options:
members: - pickle_dump - pickle_load - pickle_dumps - pickle_loads
show_source: false
heading_level: 3

### INI

Read and write INI configuration files.

::: rite.serialization.ini
options:
members: - ini_read - ini_write - ini_get - ini_set
show_source: false
heading_level: 3

## Examples

### JSON Operations

```python
from rite.serialization import json_load, json_dump, json_validate

# Load JSON from file
data = json_load("config.json")

# Save JSON to file
json_dump({"key": "value"}, "output.json")

# Validate JSON string
is_valid = json_validate('{"valid": true}')
```

### CSV Operations

```python
from rite.serialization import csv_read, csv_write

# Read CSV file
rows = csv_read("data.csv")

# Write CSV file
csv_write("output.csv", [
    ["name", "age"],
    ["Alice", 30],
    ["Bob", 25]
])
```

### TOML Operations (Python 3.11+)

```python
from rite.serialization import toml_load

# Load TOML configuration
config = toml_load("pyproject.toml")
```
