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

class LFUCache(BaseCaching):
    """will be done later"""

    def __init__(self):
        """alien documentation"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """alien documentation"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """alien documentation"""
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
