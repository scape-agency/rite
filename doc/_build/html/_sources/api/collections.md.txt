# Collections Module

The `rite.collections` module provides advanced data structures including caches, buffers, trees, and collection utilities.

## Overview

::: rite.collections
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### Cache

LRU, LFU, and TTL cache implementations.

::: rite.collections.cache
    options:
      members:
        - lru_cache
        - lfu_cache
        - ttl_cache
      show_source: false
      heading_level: 3

### Buffer

Circular and sliding window buffers.

::: rite.collections.buffer
    options:
      members:
        - circular_buffer
        - bounded_buffer
        - ring_buffer
        - sliding_window
      show_source: false
      heading_level: 3

### Dictionary Utilities

Deep operations on dictionaries.

::: rite.collections.dict
    options:
      members:
        - dict_deep_get
        - dict_deep_set
        - dict_merge
        - dict_filter
        - dict_invert
      show_source: false
      heading_level: 3

### List Utilities

Advanced list operations.

::: rite.collections.list
    options:
      members:
        - list_chunk
        - list_flatten
        - list_group_by
        - list_interleave
        - list_partition
        - list_unique
      show_source: false
      heading_level: 3

### Tree Structures

Tree and trie data structures.

::: rite.collections.tree
    options:
      members:
        - TreeNode
        - BinaryTreeNode
        - Trie
      show_source: false
      heading_level: 3

## Examples

```python
from rite.collections import (
    lru_cache,
    circular_buffer,
    dict_deep_get,
    list_chunk
)

# LRU Cache
cache = lru_cache(maxsize=100)

# Circular Buffer
buffer = circular_buffer(capacity=10)
buffer.append(1)
buffer.append(2)

# Deep dictionary access
data = {"a": {"b": {"c": 42}}}
value = dict_deep_get(data, ["a", "b", "c"])  # 42

# Chunk list
items = [1, 2, 3, 4, 5, 6]
chunks = list_chunk(items, 2)  # [[1, 2], [3, 4], [5, 6]]
```
