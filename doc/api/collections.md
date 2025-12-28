---
title: Collections API
description: Advanced data structures, buffers, caches, queues, and trees from rite.collections.
keywords: python collections, lru cache, lfu cache, ttl cache, circular buffer, sliding window, object pool
---

# Collections Module

The `rite.collections` package provides higher-level data structures and
collection utilities that extend the Python standard library.

## Overview

This section gives a high-level overview of the collections
infrastructure. Detailed APIs for each submodule are available on their
dedicated pages below.

## Submodules

- [Cache](collections/cache.md): LRU, LFU, and TTL caches.
- [Buffer](collections/buffer.md): Circular and sliding window buffers.
- [Dictionary Utilities](collections/dict.md): Deep dictionary helpers.
- [List Utilities](collections/list.md): Advanced list operations.
- [Tree Structures](collections/tree.md): Trees, binary trees, and tries.

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
