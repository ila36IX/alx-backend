#!/usr/bin/env python3
"""
LRU caching
Least recently used
"""
BaseCaching = __import__("base_caching").BaseCaching


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
