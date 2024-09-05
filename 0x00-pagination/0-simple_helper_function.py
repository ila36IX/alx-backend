#!/usr/bin/python3
"""
Pagenetion offset-limit helper
"""

def index_range(page, page_size):
    """Pagenetion offset-limit helper"""
    return (page - 1) * page_size, page * page_size
