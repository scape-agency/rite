---
title: System API
description: System-level helpers from rite.system including processes, environment, platform, paths, and shell utilities.
keywords: python system utils, subprocess, env vars, platform, shell, rite.system
---

# System Module

The `rite.system` module provides system-level operations including
process management, environment variables, platform detection, path
helpers, and shell utilities.

## Overview

This section provides a conceptual overview of the system helpers.
Submodule pages contain the full API surface.

## Submodules

- [Process](system/process.md): Run and manage system processes.
- [Environment](system/environment.md): Manage environment variables.
- [Platform](system/platform.md): Detect platform and system information.
- [Path](system/path.md): System path operations.
- [Shell](system/shell.md): Shell command utilities.

## Examples

```python
from rite.system import (
    process_run,
    env_get,
    platform_is_linux,
    shell_escape
)

# Run process
result = process_run(["ls", "-la"])

# Get environment variable
home = env_get("HOME")

# Platform detection
if platform_is_linux():
    print("Running on Linux")

# Escape shell argument
safe_arg = shell_escape("file with spaces.txt")
```
