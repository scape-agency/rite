# Filesystem Module

The `rite.filesystem` module provides file and directory operations, path management, and compression utilities.

## Overview

::: rite.filesystem
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### File Operations

Read, write, copy, move, and delete files.

::: rite.filesystem.file
options:
members: - file_read_text - file_write_text - file_read_bytes - file_write_bytes - file_copy - file_move - file_delete - file_rename - file_size_to_string
show_source: false
heading_level: 3

### Folder Operations

Manage directories and list files.

::: rite.filesystem.folder
options:
members: - folder_ensure_exists - folder_list_files - folder_size_to_string
show_source: false
heading_level: 3

### Path Utilities

Path manipulation and validation.

::: rite.filesystem.path
options:
members: - path_exists - path_is_file - path_is_dir - path_clean - path_secure - path_safe_join - path_leaf
show_source: false
heading_level: 3

### Compression

Gzip compression and decompression.

::: rite.filesystem.compress
options:
members: - compress_file - uncompress_file
show_source: false
heading_level: 3

## Examples

### File Operations

```python
from rite.filesystem import (
    file_read_text,
    file_write_text,
    file_copy,
    file_move
)

# Read text file
content = file_read_text("input.txt")

# Write text file
file_write_text("output.txt", "Hello World")

# Copy file
file_copy("source.txt", "destination.txt")

# Move file
file_move("old.txt", "new.txt")
```

### Path Management

```python
from rite.filesystem import (
    path_exists,
    path_is_file,
    path_secure,
    path_safe_join
)

# Check existence
exists = path_exists("/path/to/file.txt")

# Check if file
is_file = path_is_file("/path/to/file.txt")

# Secure path (prevent directory traversal)
safe = path_secure("../../etc/passwd")

# Safe join
joined = path_safe_join("/base", "sub", "file.txt")
```

### Compression

```python
from rite.filesystem import compress_file, uncompress_file

# Compress file
compress_file("large_file.txt", "compressed.gz")

# Decompress file
uncompress_file("compressed.gz", "restored.txt")
```
