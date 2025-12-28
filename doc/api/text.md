# Text Module

The `rite.text` module provides comprehensive text processing utilities including case conversions, slug generation, text analysis, validation, manipulation, and search operations.

## Overview

::: rite.text
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### Case Conversions

Transform text between different naming conventions and styles.

::: rite.text.case
options:
members: - to_snake_case - to_camel_case - to_pascal_case - to_kebab_case - to_constant_case - to_dot_case - to_path_case - to_title_case - to_sentence_case - to_lower_case - to_upper_case
show_source: false
heading_level: 3

### Slug Generation

Create URL-friendly slugs from text.

::: rite.text.slug
options:
members: - slugify - slug_unique - slug_add_prefix - slug_add_suffix - slug_is_valid
show_source: false
heading_level: 3

### Text Analysis

Analyze text content and structure.

::: rite.text.analysis
options:
members: - char_frequency - word_count - is_palindrome - longest_word - shortest_word - average_word_length
show_source: false
heading_level: 3

### Text Validation

Validate text format and content.

::: rite.text.validation
options:
members: - text_is_email - text_is_numeric - text_is_alpha - text_is_alphanumeric
show_source: false
heading_level: 3

### Text Manipulation

Manipulate and transform text.

::: rite.text.manipulation
options:
members: - text_truncate - text_pad_left - text_pad_right - text_wrap
show_source: false
heading_level: 3

### Text Search

Search and find patterns in text.

::: rite.text.search
options:
members: - text_contains - text_starts_with - text_ends_with - text_find - text_count
show_source: false
heading_level: 3

### Sanitization

Clean and sanitize text content.

::: rite.text.sanitize
options:
members: - sanitize - clean
show_source: false
heading_level: 3

### Morse Code

Encode and decode Morse code.

::: rite.text.morse
options:
members: - morse_encode - morse_decode
show_source: false
heading_level: 3

### Random Generation

Generate random strings.

::: rite.text.random
options:
members: - random_string - random_hex - random_alphanumeric
show_source: false
heading_level: 3

## Examples

### Basic Usage

```python
from rite.text import to_snake_case, slugify, text_truncate

# Case conversion
text = "HelloWorld"
snake = to_snake_case(text)  # "hello_world"

# Slug generation
title = "Hello World! This is a test."
slug = slugify(title)  # "hello-world-this-is-a-test"

# Text manipulation
long_text = "This is a very long text that needs truncation"
short = text_truncate(long_text, 20)  # "This is a very l..."
```

### Advanced Examples

```python
from rite.text import (
    text_is_email,
    text_pad_left,
    char_frequency,
    text_contains
)

# Validation
email = "user@example.com"
is_valid = text_is_email(email)  # True

# Padding
number = "42"
padded = text_pad_left(number, 5, "0")  # "00042"

# Analysis
text = "hello world"
freq = char_frequency(text)  # {'h': 1, 'e': 1, 'l': 3, ...}

# Search
haystack = "The quick brown fox"
found = text_contains(haystack, "quick")  # True
```
