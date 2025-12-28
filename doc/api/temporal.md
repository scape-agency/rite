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
::: rite.temporal.formatting
options:
members: - format_iso8601 - format_rfc3339 - format_human_readable
show_source: false
heading_level: 3

## Examples

## Overview

This section introduces the temporal helpers conceptually. The detailed
APIs are documented on the submodule pages.

## Submodules

- [Datetime](temporal/datetime.md): Work with aware and naive
    datetimes.
- [Duration](temporal/duration.md): Represent durations and time spans.
- [Timezone](temporal/timezone.md): Timezone utilities.
- [Calendar](temporal/calendar.md): Calendar and date range helpers.
- [Formatting](temporal/formatting.md): Date and time formatting
    utilities.

## Examples

```python
from rite.temporal import datetime_now, duration_from_hours

now = datetime_now()
three_hours = duration_from_hours(3)

```python
from rite.temporal import (
    datetime_now,
    show_root_heading: true
    show_source: false
    heading_level: 2
    show_submodules: false

## Submodules

- [Datetime](temporal/datetime.md): Work with aware and naive datetimes.
- [Duration](temporal/duration.md): Represent durations and time spans.
- [Timezone](temporal/timezone.md): Timezone utilities.
- [Calendar](temporal/calendar.md): Calendar and date range helpers.
- [Formatting](temporal/formatting.md): Date and time formatting utilities.
three_hours = duration_from_hours(3)
