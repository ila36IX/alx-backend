#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """Pagenetion offset-limit helper"""
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return slice of data for a page"""
        assert (type(page), type(page_size)) == (int, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia as the engine"""
        data = self.get_page(page, page_size)
        hyper = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'total_pages': math.ceil(len(self.__dataset) / page_size)
        }
        if page == 1:
            hyper['prev_page'] = None
        else:
            hyper['prev_page'] = page - 1

        if page >= hyper['total_pages']:
            hyper['next_page'] = None
        else:
            hyper['next_page'] = page + 1
        return hyper
