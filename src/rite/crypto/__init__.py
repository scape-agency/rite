# =============================================================================
# Docstring
# =============================================================================

"""
Cryptography Module
===================

This module provides cryptographic operations similar to Python's
hashlib, secrets, and hmac modules.

Functions will include:
- Hashing (MD5, SHA, etc.)
- Simple ciphers (Caesar, substitution)
- Base64, hex encoding (stdlib wrappers)

Example:
    >>> from rite.crypto import hash_sha256
    >>> hash_sha256("hello")
    '2cf24dba5fb0a...'

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local - Ciphers
from .cipher import (
    decode_atbash_cipher,
    decode_autokey_cipher,
    decode_baconian_cipher,
    decode_caesar_cipher,
    decode_four_square_cipher,
    decode_playfair_cipher,
    decode_rail_fence_cipher,
    decode_rot13_cipher,
    decode_scytale_cipher,
    decode_transposition_cipher,
    decode_vigenere_cipher,
    decode_xor_cipher,
    encode_atbash_cipher,
    encode_autokey_cipher,
    encode_baconian_cipher,
    encode_caesar_cipher,
    encode_four_square_cipher,
    encode_playfair_cipher,
    encode_rail_fence_cipher,
    encode_rot13_cipher,
    encode_scytale_cipher,
    encode_transposition_cipher,
    encode_vigenere_cipher,
    encode_xor_cipher,
    four_square_cipher_pair,
)

# Import | Local - Hashing
from .hash.hash_sha256 import sha256_hash
from .hash.hash_sha512 import sha512_hash

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    # Hashing
    "sha256_hash",
    "sha512_hash",
    # Ciphers - Atbash
    "decode_atbash_cipher",
    "encode_atbash_cipher",
    # Ciphers - Autokey
    "decode_autokey_cipher",
    "encode_autokey_cipher",
    # Ciphers - Baconian
    "decode_baconian_cipher",
    "encode_baconian_cipher",
    # Ciphers - Caesar
    "decode_caesar_cipher",
    "encode_caesar_cipher",
    # Ciphers - Four Square
    "decode_four_square_cipher",
    "encode_four_square_cipher",
    "four_square_cipher_pair",
    # Ciphers - Playfair
    "decode_playfair_cipher",
    "encode_playfair_cipher",
    # Ciphers - Rail Fence
    "decode_rail_fence_cipher",
    "encode_rail_fence_cipher",
    # Ciphers - ROT13
    "decode_rot13_cipher",
    "encode_rot13_cipher",
    # Ciphers - Scytale
    "decode_scytale_cipher",
    "encode_scytale_cipher",
    # Ciphers - Transposition
    "decode_transposition_cipher",
    "encode_transposition_cipher",
    # Ciphers - Vigenère
    "decode_vigenere_cipher",
    "encode_vigenere_cipher",
    # Ciphers - XOR
    "decode_xor_cipher",
    "encode_xor_cipher",
]
