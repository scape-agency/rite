#!/usr/bin/env python3
# =============================================================================
# Import Check Script
# =============================================================================

"""Temporary script to check imports from rite.filesystem module."""

# Import | Local Modules
from src.rite.filesystem import (
    compress_file,
    copy_file,
    copy_files,
    create_spooled_temporary_file,
    delete_file,
    extension_normalize,
    EXTENSION_REGEX,
    extension_validate,
    file_read_bytes,
    file_read_text,
    file_size_to_string,
    file_write_bytes,
    file_write_text,
    move_file,
    path_clean,
    path_exists,
    path_is_dir,
    path_is_file,
    path_leaf,
    path_safe_join,
    path_secure,
    rename_file,
    uncompress_file,
)

print("Top-level imports OK")
