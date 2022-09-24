#!/usr/bin/env python3
"""
    Module with function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: list int and float
        Return:
            float sum of list
    """

    return float(sum(mxd_lst))
