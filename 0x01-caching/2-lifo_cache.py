#!/usr/bin/env python3
"""
LIFO caching
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


class LIFOCache(BaseCaching):
    """LIFO Caching"""
    MAX_ITEMS = 4

    def __init__(self):
        """init"""
        super().__init__()
        self.LIFO = []

    def put(self, key, item):
        """insert into stack if it's not full"""
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
