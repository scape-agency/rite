# -*- coding: utf-8 -*-

"""Compression helpers for filesystem utilities."""

from .file_gzip_compress import compress_file
from .file_gzip_uncompress import uncompress_file

__all__ = [
    "compress_file",
    "uncompress_file",
]
