#!/usr/bin/env python3
"""
BaseCaching module
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """implemente the getting and setting functionality"""

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
