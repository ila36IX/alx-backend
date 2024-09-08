#!/usr/bin/env python3
"""
LFU + LRU
Least frequently used + least recently used
Discard the least frequency used item (LFU algorithm)
if more than 1 item found to discard, the LRU algorithm will be used
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least frequently used + least recently used"""

    def __init__(self):
        """init least frequently used cache algorithm"""
        super().__init__()
        self.lru = []
        self.lfu = {}

    def put(self, key, item):
        """Insert new element in the cache, and discord least freaquanlty used
        key if the cache reaches it's capacity
        """
        if key is None or item is None:
            return
        if key in self.lfu:
            self.lfu[key] += 1
            self.lru.remove(key)
            self.lru.insert(0, key)
            self.cache_data[key] = item
            return
        if len(self.lru) >= self.MAX_ITEMS:
            most_freq = []
            for k, freq in self.lfu.items():
                if len(most_freq) == 0:
                    most_freq.append(k)
                elif freq < self.lfu[most_freq[0]]:
                    most_freq = [k]
                elif freq == self.lfu[most_freq[0]]:
                    most_freq.append(k)
            if len(most_freq) > 1:
                discard_key = most_freq[0]
                discard_key_index = len(most_freq) - 1
                for k in most_freq:
                    prob_index = self.lru.index(k)
                    if prob_index > discard_key_index:
                        discard_key_index = prob_index
                        discard_key = k
                print('DISCARD:', discard_key)
                self.lfu.pop(discard_key)
                self.lru.remove(discard_key)
                self.cache_data.pop(discard_key)
            else:
                print('DISCARD:', most_freq[0])
                self.lfu.pop(most_freq[0])
                self.lru.remove(most_freq[0])
                self.cache_data.pop(most_freq[0])
        self.cache_data[key] = item
        self.lru.insert(0, key)
        self.lfu[key] = 1

    def get(self, key):
        """Get item using key from the cache"""
        if key is None:
            return None
        if key not in self.lru:
            return
        self.lru.remove(key)
        self.lru.insert(0, key)
        self.lfu[key] += 1
        return self.cache_data[key]
