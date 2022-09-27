#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Args:
            index: index
            page_size: page size

        Returns:
            dict with data
        """
        result_dataset: List = []
        indexed_data: Dict = self.indexed_dataset()
        keys_list: List = list(indexed_data.keys())
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in indexed_data:
            start_index = keys_list[index]
        else:
            start_index = index

        for _index in range(start_index, start_index + page_size):
            if index not in indexed_data:
                result_dataset.append(indexed_data[keys_list[_index]])
            else:
                result_dataset.append(indexed_data[_index])

        next_index: int = index + page_size

        if index not in keys_list:
            next_index = keys_list[next_index]

        return {
            'index': index,
            'data': result_dataset,
            'page_size': len(result_dataset),
            'next_index': next_index
        }
