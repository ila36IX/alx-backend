#!/usr/bin/env python3
"""
LRU caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used by keeps track of the most recently used items and
    discards the least recently used ones when the cache reaches its capacity
    """
    def __init__(self):
        """init least recetly used cache data structure"""
        super().__init__()
        self.LRU = []

    def put(self, key, item):
        """Insert new key-value in the cache system and discord lru if reaches
        its capacity
        """
        if key is None or item is None:
            return
        if key in self.LRU:
            self.LRU.remove(key)
            self.LRU.insert(0, key)
            self.cache_data[key] = item
            return

        if len(self.LRU) >= self.MAX_ITEMS:
            evict_key = self.LRU.pop(-1)
            print('DISCARD:', evict_key)
            del self.cache_data[evict_key]
        self.LRU.insert(0, key)
        self.cache_data[key] = item

    def get(self, key):
        """Get new value using key in the cache system and update lru key"""
        if key not in self.LRU:
            return
        self.LRU.remove(key)
        self.LRU.insert(0, key)
        return self.cache_data[key]
