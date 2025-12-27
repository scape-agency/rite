# Temporal Module

The `rite.temporal` module provides comprehensive date, time, and duration management utilities.

## Overview

::: rite.temporal
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### DateTime Operations

Work with datetime objects.

::: rite.temporal.datetime
    options:
      members:
        - datetime_now
        - datetime_from_timestamp
        - datetime_to_timestamp
        - datetime_parse
        - datetime_format
        - datetime_to_iso
      show_source: false
      heading_level: 3

### Duration Management

Create and manage time durations.

::: rite.temporal.duration
    options:
      members:
        - duration_from_seconds
        - duration_from_minutes
        - duration_from_hours
        - duration_from_days
        - duration_to_seconds
      show_source: false
      heading_level: 3

### Timezone Handling

Manage timezones and conversions.

::: rite.temporal.timezone
    options:
      members:
        - timezone_get
        - timezone_convert
        - timezone_list
      show_source: false
      heading_level: 3

### Calendar Utilities

Calendar and date calculations.

::: rite.temporal.calendar
    options:
      members:
        - calendar_is_leap_year
        - calendar_month_days
        - calendar_weekday
      show_source: false
      heading_level: 3

### Formatting

Format dates and times.

::: rite.temporal.formatting
    options:
      members:
        - format_iso8601
        - format_rfc3339
        - format_human_readable
      show_source: false
      heading_level: 3

## Examples

### Basic Usage

```python
from rite.temporal import (
    datetime_now,
    datetime_to_iso,
    duration_from_hours,
    calendar_is_leap_year
)

# Get current datetime
now = datetime_now()

# Convert to ISO format
iso_string = datetime_to_iso(now)

# Create duration
three_hours = duration_from_hours(3)

# Check leap year
is_leap = calendar_is_leap_year(2024)  # True
```

### Working with Timezones

```python
from rite.temporal import (
    datetime_now,
    timezone_get,
    timezone_convert,
    timezone_list
)
from datetime import datetime

# Get current datetime with timezone
now = datetime_now()
utc_tz = timezone_get("UTC")

# Convert between timezones
ny_tz = timezone_get("America/New_York")
converted = timezone_convert(now, utc_tz, ny_tz)

# List available timezones
all_zones = timezone_list()
```
