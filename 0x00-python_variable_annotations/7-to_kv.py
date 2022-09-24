#!/usr/bin/env python3
"""
    Module with function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: str parameter
            v: int or float parameter
        Return:
            Tuple of str and int or flaot
    """

    return k, float(v)**2
