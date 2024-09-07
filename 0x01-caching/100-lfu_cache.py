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
        self.lfu = {}
        self.lru = []

    def put(self, key, item):

