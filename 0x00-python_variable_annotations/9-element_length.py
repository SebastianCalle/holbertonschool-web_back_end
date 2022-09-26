#!/usr/bin/env python3
"""
    Module with annotate function
"""
from typing import Iterable, Sequence, List, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst: str parameter
        Return:
            Callable
    """
    return [(i, len(i)) for i in lst]
