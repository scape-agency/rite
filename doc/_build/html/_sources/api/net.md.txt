# Net Module

The `rite.net` module provides network utilities including URL handling, HTTP operations, and validation.

## Overview

::: rite.net
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### URL

Parse and manipulate URLs.

::: rite.net.url
    options:
      members:
        - url_parse
        - url_build
        - url_encode
        - url_decode
        - url_parse_query
      show_source: false
      heading_level: 3

### HTTP

HTTP utilities and status codes.

::: rite.net.http
    options:
      members:
        - http_status_code
        - http_is_method
        - http_parse_headers
      show_source: false
      heading_level: 3

### Validation

Validate network-related formats.

::: rite.net.validation
    options:
      members:
        - validation_is_url
        - validation_is_email
        - validation_is_ipv4
        - validation_is_port
      show_source: false
      heading_level: 3

## Examples

```python
from rite.net import (
    url_parse,
    validation_is_url,
    http_status_code
)

# Parse URL
parts = url_parse("https://example.com/path?key=value")

# Validate URL
is_valid = validation_is_url("https://example.com")

# Get HTTP status message
message = http_status_code(404)  # "Not Found"
```
