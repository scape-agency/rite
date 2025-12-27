# Markup Module

The `rite.markup` module provides utilities for working with HTML, XML, and Markdown.

## Overview

::: rite.markup
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### HTML

HTML manipulation and sanitization.

::: rite.markup.html
    options:
      members:
        - html_escape
        - html_unescape
        - html_strip_tags
        - html_clean
      show_source: false
      heading_level: 3

### XML

XML parsing and formatting.

::: rite.markup.xml
    options:
      members:
        - xml_escape
        - xml_unescape
        - xml_format
      show_source: false
      heading_level: 3

### Markdown

Markdown processing.

::: rite.markup.markdown
    options:
      members:
        - markdown_escape
        - markdown_to_html
      show_source: false
      heading_level: 3

### Entities

HTML entity encoding/decoding.

::: rite.markup.entities
    options:
      members:
        - entities_encode
        - entities_decode
      show_source: false
      heading_level: 3

## Examples

```python
from rite.markup import (
    html_escape,
    xml_format,
    markdown_to_html
)

# Escape HTML
safe = html_escape("<script>alert('xss')</script>")

# Format XML
formatted = xml_format("<root><child>text</child></root>")

# Convert Markdown
html = markdown_to_html("# Heading\n\nParagraph")
```
