#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""
    MAX_ITEMS = 4

    def __init__(self):
        """Init"""
        super().__init__()
        self.FIFO = []

    def put(self, key, item):
        """get item by key"""
        if key is None or item is None:
            return
        if key not in self.FIFO:
            self.FIFO.insert(0, key)
            if len(self.FIFO) > self.MAX_ITEMS:
                discard_key = self.FIFO.pop()
                print('DISCARD:', discard_key)
                self.cache_data.pop(discard_key)
        self.cache_data[key] = item

    def get(self, key):
        """Get cached item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
