#!/usr/bin/env python3
"""
tseitng
tseitng
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used by keeps track of the most recently used items and
    discards the most recently used one when the cache reaches its capacity
    """
    def __init__(self):
        """init most recetly used cache data structure"""
        super().__init__()
        self.MRU = []

    def put(self, key, item):
        """Insert new key-value in the cache system and discord mru if reaches
        its capacity
        """
        if key is None or item is None:
            return
        if key in self.MRU:
            self.MRU.remove(key)
            self.MRU.insert(0, key)
            self.cache_data[key] = item
            return

        if len(self.MRU) >= self.MAX_ITEMS:
            evict_key = self.MRU.pop(0)
            print('DISCARD:', evict_key)
            del self.cache_data[evict_key]
        self.MRU.insert(0, key)
        self.cache_data[key] = item

    def get(self, key):
        """Get new value using key in the cache system and update mru key"""
        if key not in self.MRU:
            return
        self.MRU.remove(key)
        self.MRU.insert(0, key)
        return self.cache_data[key]
