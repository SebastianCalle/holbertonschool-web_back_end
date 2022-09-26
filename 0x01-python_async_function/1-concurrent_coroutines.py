#!/usr/bin/env python3
"""
    Module with concurrent coroutines
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: times
        max_delay:  max delay

    Returns:
        list of floats
    """
    result = []
    for _ in range(n):
        result.append(await wait_random(max_delay))

    return result


