#!/usr/bin/env python3
"""
LRU caching
Least recently used
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        err = "put must be implemented in your cache class"
        raise NotImplementedError(err)

    def get(self, key):
        """ Get an item by key
        """
        err = "get must be implemented in your cache class"
        raise NotImplementedError(err)

class LRUCache(BaseCaching):
    """alien doc"""

    def __init__(self):
        """alien doc"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """setting item"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Getting item"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
