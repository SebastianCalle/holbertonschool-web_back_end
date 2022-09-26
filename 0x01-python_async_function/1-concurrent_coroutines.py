#!/usr/bin/env python3
"""
    Module with concurrent coroutines
"""
import asyncio
from typing import List, Tuple

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: times
        max_delay:  max delay

    Returns:
        list of floats
    """
    randoms: Tuple[asyncio.Task, ...] = \
        tuple([asyncio.create_task(wait_random(
            max_delay)) for _ in range(n)])

    result: List[float] = []

    for res in asyncio.as_completed(randoms):
        result.append(await res)

    return result
