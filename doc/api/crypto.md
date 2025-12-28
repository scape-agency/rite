---
title: Crypto API
description: Cryptographic helpers from rite.crypto including hashing, HMAC, and UUID utilities.
keywords: python crypto, hashing, hmac, uuid, rite.crypto
---

# Crypto Module

The `rite.crypto` package provides hashing, HMAC, UUID, and other
cryptographic helpers built entirely on the Python standard library.

## Overview

This section introduces the cryptographic helpers at a high level.
Each submodule page contains the detailed API reference.

## Submodules

- [Hash](crypto/hash.md): Cryptographic hash functions.
- [UUID](crypto/uuid.md): Generate and validate UUIDs.
- [Random](crypto/random.md): Cryptographically secure random generation.
- [Cipher](crypto/cipher.md): Classical cipher implementations.

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
