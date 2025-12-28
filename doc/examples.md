# Usage Examples

This guide provides practical examples for common use cases across all Rite modules.

## Cryptography

### UUID Operations

```python
from rite.crypto.uuid import uuid_hex, uuid_int, uuid_base64

# Generate hexadecimal UUID
hex_id = uuid_hex()
# '550e8400e29b41d4a716446655440000'

# Generate integer UUID
int_id = uuid_int()
# 113059749145936325402354257176981405696

# Generate base64 UUID
b64_id = uuid_base64()
# 'VQ6EAOKbQdSnFkRmVUQAAA'
```

### Hashing

```python
from rite.crypto.hash import hash_sha256, hash_md5, hash_blake2b

# SHA-256 hash
sha_hash = hash_sha256("password123")
# 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'

# MD5 hash
md5_hash = hash_md5("data")
# '8d777f385d3dfec8815d20f7496026dc'

# BLAKE2b hash (faster than SHA-256)
blake_hash = hash_blake2b("secure_data")
# '7a42b...'
```

### HMAC

```python
from rite.crypto.hmac import hmac_sha256, hmac_sha512

# Generate HMAC with secret key
signature = hmac_sha256("message", "secret_key")
# 'a6c8f...'

# Stronger HMAC
strong_sig = hmac_sha512("critical_data", "strong_secret")
# 'b8d9e...'
```

## Filesystem Operations

### File Operations

```python
from rite.filesystem.file import (
    file_copy,
    file_move,
    file_delete,
    file_exists,
    file_read,
    file_write,
)
from pathlib import Path

# Check if file exists
if file_exists("config.json"):
    # Read file
    content = file_read("config.json")

    # Copy file
    file_copy("config.json", "config.backup.json")

    # Move file
    file_move("old_location.txt", "new_location.txt")

    # Write file
    file_write("output.txt", "Hello, World!")

    # Delete file
    file_delete("temp.txt")
```

### Directory Operations

```python
from rite.filesystem.folder import (
    folder_create,
    folder_delete,
    folder_list_files,
    folder_list_dirs,
    folder_size,
)

# Create directory
folder_create("data/processed")

# List files in directory
files = folder_list_files("data/")
# ['file1.txt', 'file2.txt']

# List subdirectories
dirs = folder_list_dirs("src/")
# ['crypto', 'filesystem', 'text']

# Get directory size
size = folder_size("data/")
# 1048576  # bytes

# Delete directory
folder_delete("temp/")
```

### Path Utilities

```python
from rite.filesystem.path import (
    path_join,
    path_absolute,
    path_normalize,
    path_extension,
    path_basename,
)

# Join paths
full_path = path_join("data", "processed", "file.txt")
# 'data/processed/file.txt'

# Get absolute path
abs_path = path_absolute("../data/file.txt")
# '/home/user/project/data/file.txt'

# Normalize path
clean_path = path_normalize("data/../data/./file.txt")
# 'data/file.txt'

# Get file extension
ext = path_extension("document.pdf")
# '.pdf'

# Get basename
name = path_basename("/path/to/file.txt")
# 'file.txt'
```

## Text Processing

### Slug Generation

```python
from rite.text.slug import slug_generate, slug_is_valid, slug_normalize

# Generate slug
slug = slug_generate("Hello World!")
# 'hello-world'

# With special characters
slug = slug_generate("Café & Restaurant")
# 'cafe-restaurant'

# Validate slug
is_valid = slug_is_valid("hello-world")
# True

is_valid = slug_is_valid("Hello World!")
# False

# Normalize existing slug
normalized = slug_normalize("HELLO___WORLD")
# 'hello-world'
```

### Case Conversion

```python
from rite.text.case import (
    case_to_snake,
    case_to_camel,
    case_to_pascal,
    case_to_kebab,
    case_to_title,
)

text = "helloWorld"

# Snake case
snake = case_to_snake(text)
# 'hello_world'

# Camel case
camel = case_to_camel("hello_world")
# 'helloWorld'

# Pascal case
pascal = case_to_pascal("hello_world")
# 'HelloWorld'

# Kebab case
kebab = case_to_kebab("helloWorld")
# 'hello-world'

# Title case
title = case_to_title("hello world")
# 'Hello World'
```

### Text Sanitization

```python
from rite.text.sanitize import (
    sanitize_html,
    sanitize_sql,
    sanitize_filename,
    sanitize_email,
)

# Remove HTML tags
clean = sanitize_html("<p>Hello <b>World</b></p>")
# 'Hello World'

# Escape SQL
safe_sql = sanitize_sql("'; DROP TABLE users; --")
# '\'; DROP TABLE users; --'

# Clean filename
filename = sanitize_filename("file: name?.txt")
# 'file_name.txt'

# Validate and clean email
email = sanitize_email("  User@Example.COM  ")
# 'user@example.com'
```

### Text Analysis

```python
from rite.text.analysis import (
    word_count,
    char_frequency,
    longest_word,
    shortest_word,
    average_word_length,
    is_palindrome,
)

text = "The quick brown fox jumps over the lazy dog"

# Word count
count = word_count(text)
# 9

# Character frequency
freq = char_frequency(text)
# {'t': 2, 'h': 2, 'e': 3, ...}

# Longest word
longest = longest_word(text)
# 'quick'

# Shortest word
shortest = shortest_word(text)
# 'the'

# Average word length
avg = average_word_length(text)
# 3.88...

# Check palindrome
is_pal = is_palindrome("racecar")
# True
```

## Collections

### List Operations

```python
from rite.collections.list import (
    list_unique,
    list_flatten,
    list_chunk,
    list_group_by,
)

# Remove duplicates
unique = list_unique([1, 2, 2, 3, 3, 3])
# [1, 2, 3]

# Flatten nested lists
flat = list_flatten([[1, 2], [3, 4], [5]])
# [1, 2, 3, 4, 5]

# Chunk list
chunks = list_chunk([1, 2, 3, 4, 5], size=2)
# [[1, 2], [3, 4], [5]]

# Group by key
data = [
    {"type": "fruit", "name": "apple"},
    {"type": "fruit", "name": "banana"},
    {"type": "vegetable", "name": "carrot"},
]
grouped = list_group_by(data, key="type")
# {
#     'fruit': [{'type': 'fruit', 'name': 'apple'}, ...],
#     'vegetable': [{'type': 'vegetable', 'name': 'carrot'}]
# }
```

### Dictionary Operations

```python
from rite.collections.dict import (
    dict_merge,
    dict_filter,
    dict_invert,
    dict_deep_get,
)

# Merge dictionaries
merged = dict_merge(
    {"a": 1, "b": 2},
    {"b": 3, "c": 4}
)
# {'a': 1, 'b': 3, 'c': 4}

# Filter dictionary
filtered = dict_filter(
    {"a": 1, "b": 2, "c": 3},
    lambda k, v: v > 1
)
# {'b': 2, 'c': 3}

# Invert dictionary
inverted = dict_invert({"a": 1, "b": 2})
# {1: 'a', 2: 'b'}

# Deep get with nested keys
data = {"user": {"profile": {"name": "John"}}}
name = dict_deep_get(data, ["user", "profile", "name"])
# 'John'
```

## Conversions

### Type Conversions

```python
from rite.conversion.types import (
    to_int,
    to_float,
    to_bool,
    to_string,
)

# Safe integer conversion
num = to_int("123", default=0)
# 123

invalid = to_int("abc", default=0)
# 0

# Float conversion
value = to_float("3.14", default=0.0)
# 3.14

# Boolean conversion
flag = to_bool("true")  # or "1", "yes", "on"
# True

flag = to_bool("false")  # or "0", "no", "off"
# False

# String conversion
text = to_string(123)
# '123'
```

### Data Format Conversions

```python
from rite.conversion.format import (
    json_to_dict,
    dict_to_json,
    csv_to_list,
    list_to_csv,
)

# JSON to dictionary
data = json_to_dict('{"name": "John", "age": 30}')
# {'name': 'John', 'age': 30}

# Dictionary to JSON
json_str = dict_to_json({"name": "John", "age": 30})
# '{"name": "John", "age": 30}'

# CSV to list
rows = csv_to_list("name,age\nJohn,30\nJane,25")
# [['name', 'age'], ['John', '30'], ['Jane', '25']]

# List to CSV
csv_str = list_to_csv([['name', 'age'], ['John', '30']])
# 'name,age\nJohn,30'
```

## Numeric Operations

### Math Utilities

```python
from rite.numeric.math import (
    clamp,
    round_to,
    is_even,
    is_odd,
    percentage,
)

# Clamp value within range
value = clamp(15, min_val=0, max_val=10)
# 10

# Round to specific decimal places
rounded = round_to(3.14159, decimals=2)
# 3.14

# Check even/odd
is_even(4)  # True
is_odd(4)   # False

# Calculate percentage
pct = percentage(25, 100)
# 25.0
```

### Statistics

```python
from rite.numeric.stats import (
    mean,
    median,
    mode,
    std_dev,
)

data = [1, 2, 3, 4, 5]

# Mean (average)
avg = mean(data)
# 3.0

# Median (middle value)
mid = median(data)
# 3

# Mode (most common)
common = mode([1, 1, 2, 3, 3, 3])
# 3

# Standard deviation
std = std_dev(data)
# 1.41...
```

## Temporal Operations

### Date/Time Utilities

```python
from rite.temporal.datetime import (
    now,
    today,
    format_datetime,
    parse_datetime,
    add_days,
    diff_days,
)

# Current datetime
current = now()
# datetime(2024, 1, 15, 10, 30, 0)

# Today's date
date = today()
# date(2024, 1, 15)

# Format datetime
formatted = format_datetime(current, "%Y-%m-%d %H:%M")
# '2024-01-15 10:30'

# Parse datetime
parsed = parse_datetime("2024-01-15", "%Y-%m-%d")
# datetime(2024, 1, 15, 0, 0, 0)

# Add days
future = add_days(date, 7)
# date(2024, 1, 22)

# Calculate difference
days = diff_days(date1, date2)
# 7
```

### Timestamp Operations

```python
from rite.temporal.timestamp import (
    unix_timestamp,
    from_timestamp,
    timestamp_to_iso,
)

# Get Unix timestamp
ts = unix_timestamp()
# 1705316400

# Convert from timestamp
dt = from_timestamp(1705316400)
# datetime(2024, 1, 15, 10, 0, 0)

# Timestamp to ISO format
iso = timestamp_to_iso(1705316400)
# '2024-01-15T10:00:00Z'
```

## Complete Example: Data Processing Pipeline

```python
from rite.filesystem.file import file_read, file_write
from rite.conversion.format import json_to_dict, dict_to_json
from rite.text.case import case_to_snake
from rite.collections.dict import dict_filter
from rite.crypto.hash import hash_sha256
from pathlib import Path


def process_user_data(input_file: str, output_file: str) -> None:
    """
    Complete data processing pipeline.

    Args:
        input_file: Input JSON file path.
        output_file: Output JSON file path.
    """
    # Read input file
    raw_data = file_read(input_file)

    # Parse JSON
    data = json_to_dict(raw_data)

    # Process each user
    processed_users = []
    for user in data.get("users", []):
        # Normalize keys to snake_case
        normalized = {
            case_to_snake(k): v
            for k, v in user.items()
        }

        # Filter out empty values
        cleaned = dict_filter(
            normalized,
            lambda k, v: v is not None and v != ""
        )

        # Add ID hash
        cleaned["id_hash"] = hash_sha256(
            str(cleaned.get("email", ""))
        )

        processed_users.append(cleaned)

    # Create output data
    output = {
        "processed_at": unix_timestamp(),
        "count": len(processed_users),
        "users": processed_users
    }

    # Write to file
    json_output = dict_to_json(output, indent=2)
    file_write(output_file, json_output)

    print(f"Processed {len(processed_users)} users")


# Usage
process_user_data("input.json", "output.json")
```

## See Also

-   [Getting Started Guide](getting-started.md)
-   [API Documentation](api/index.md)
-   [Contributing Guide](contributing.md)
