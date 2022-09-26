#!/usr/bin/env python3
"""
    Module with annotate function
"""
from types import NoneType
from typing import Sequence, Union, Any, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
