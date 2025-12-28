# System Module

The `rite.system` module provides system-level operations including process management, environment variables, and platform detection.

## Overview

::: rite.system
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### Process

Run and manage system processes.

::: rite.system.process
options:
members: - process_run - process_call - process_check_output
show_source: false
heading_level: 3

### Environment

Manage environment variables.

::: rite.system.environment
options:
members: - env_get - env_set - env_delete - env_list
show_source: false
heading_level: 3

### Platform

Detect platform and system information.

::: rite.system.platform
options:
members: - platform_name - platform_architecture - platform_is_windows - platform_is_linux - platform_is_macos - platform_python_version
show_source: false
heading_level: 3

### Path

System path operations.

::: rite.system.path
options:
members: - path_exists - path_is_file - path_is_dir - path_absolute - path_join
show_source: false
heading_level: 3

### Shell

Shell command utilities.

::: rite.system.shell
options:
members: - shell_escape - shell_split - shell_join
show_source: false
heading_level: 3

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
