# Diagnostics Module

The `rite.diagnostics` module provides logging, profiling, error handling, and debugging utilities.

## Overview

::: rite.diagnostics
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### Logging

Structured logging utilities.

::: rite.diagnostics.logging
    options:
      members:
        - logging_to_console
        - logging_to_file
        - logging_structured
        - logging_with_context
      show_source: false
      heading_level: 3

### Profiling

Performance profiling tools.

::: rite.diagnostics.profiling
    options:
      members:
        - profiling_timer
        - profiling_stopwatch
        - profiling_memory
        - profiling_count_calls
      show_source: false
      heading_level: 3

### Error Handling

Error management utilities.

::: rite.diagnostics.errors
    options:
      members:
        - errors_catch
        - errors_retry
        - errors_get_chain
        - errors_format_traceback
      show_source: false
      heading_level: 3

### Metrics

Application metrics collection.

::: rite.diagnostics.metrics
    options:
      members:
        - metrics_counter
        - metrics_gauge
        - metrics_timer
        - metrics_histogram
      show_source: false
      heading_level: 3

## Examples

```python
from rite.diagnostics import (
    profiling_timer,
    errors_retry,
    metrics_counter
)

# Time function execution
@profiling_timer
def slow_function():
    # ... code ...
    pass

# Retry on failure
@errors_retry(max_attempts=3)
def unstable_operation():
    # ... code ...
    pass

# Count metrics
counter = metrics_counter("requests")
counter.increment()
```
