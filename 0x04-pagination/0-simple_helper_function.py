#!/usr/bin/env python3
"""
    Module with function index_range
"""
from typing import Tuple


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
