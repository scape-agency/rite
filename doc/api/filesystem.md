---
title: Filesystem API
description: File, folder, path, compress, and mimetype utilities from rite.filesystem.
keywords: python filesystem, file utils, folder utils, path utils, mimetype, rite.filesystem
---

# Filesystem Module

The `rite.filesystem` module provides file and directory operations, path
management, compression utilities, and mimetype helpers.

## Overview

This section describes the filesystem abstractions conceptually.
Detailed APIs live on the individual submodule pages.

## Submodules

- [File](filesystem/file.md): Read, write, copy, move, and delete files.
- [Folder](filesystem/folder.md): Manage directories and list files.
- [Path](filesystem/path.md): Path manipulation and validation.
- [Compress](filesystem/compress.md): Gzip compression and decompression.

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
