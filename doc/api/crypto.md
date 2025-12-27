# Crypto Module

The `rite.crypto` module provides cryptographic operations including hashing, ciphers, UUIDs, and secure random generation.

## Overview

::: rite.crypto
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### Hashing

Cryptographic hash functions.

::: rite.crypto.hash
    options:
      members:
        - hash_md5
        - hash_sha1
        - hash_sha256
        - hash_sha384
        - hash_sha512
        - hash_sha3_256
        - hash_sha3_512
        - hash_blake2b
        - hash_blake2s
      show_source: false
      heading_level: 3

### UUID Generation

Generate and validate UUIDs.

::: rite.crypto.uuid
    options:
      members:
        - uuid_random
        - uuid_hex
        - uuid_string
        - uuid_from_name
        - uuid_is_valid
        - uuid_is_random
        - uuid_get_version
      show_source: false
      heading_level: 3

### Secure Random

Cryptographically secure random generation.

::: rite.crypto.random
    options:
      members:
        - random_bytes
        - random_int
        - random_hex
        - random_choice
        - random_urlsafe
      show_source: false
      heading_level: 3

### Ciphers

Classical cipher implementations.

::: rite.crypto.cipher
    options:
      members:
        - cipher_caesar
        - cipher_rot13
        - cipher_vigenere
        - cipher_atbash
        - cipher_xor
      show_source: false
      heading_level: 3

## Examples

### Hashing

```python
from rite.crypto import hash_sha256, hash_blake2b

# SHA-256 hash
data = "sensitive data"
hashed = hash_sha256(data)

# BLAKE2b hash
hashed_b = hash_blake2b(data.encode())
```

### UUID Operations

```python
from rite.crypto import (
    uuid_random,
    uuid_hex,
    uuid_is_valid,
    uuid_from_name
)

# Generate random UUID
random_id = uuid_random()

# Get hex representation
hex_id = uuid_hex(random_id)

# Validate UUID
is_valid = uuid_is_valid(hex_id)

# Generate UUID from name
namespace_uuid = uuid_random()
name_uuid = uuid_from_name(namespace_uuid, "example.com")
```

### Secure Random Generation

```python
from rite.crypto import random_bytes, random_hex, random_int

# Generate random bytes
secret_key = random_bytes(32)

# Generate random hex string
token = random_hex(16)

# Generate random integer
nonce = random_int(0, 1000000)
```
