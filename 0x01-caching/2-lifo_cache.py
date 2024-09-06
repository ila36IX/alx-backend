#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""
    MAX_ITEMS = 4

    def __init__(self):
        """init"""
        super().__init__()
        self.LIFO = []

    def put(self, key, item):
        """insert into stack if it's not full"""
        if key is None or item is None:
            return
        if key not in self.LIFO:
            if len(self.LIFO) == self.MAX_ITEMS:
                discord_key = self.LIFO.pop(-1)
                self.cache_data.pop(discord_key)
                print('DISCARD:', discord_key)
            self.LIFO.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get cached item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
