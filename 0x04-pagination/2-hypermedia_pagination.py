#!/usr/bin/env python3
"""
    Module with class Server
"""
import csv
import math
from typing import List, Tuple, Any, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page: first parameter
        page_size: second parameter
    Returns:
        Tuple with start and end index
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return start_index, end_index


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
        """
        Args:
            page: number page
            page_size: page size
        Returns:
            List of rows
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        try:
            self.dataset()
            return self.__dataset[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Args:
            page: number page
            page_size: page size
        Returns:
            dict with keys
        """
        self.dataset()
        data = self.get_page(page, page_size)
        more_data = self.get_page(page + 1, page_size)

        response: Dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if more_data else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }

        return response
