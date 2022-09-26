#!/usr/bin/env python3
"""
    Module basic asyncio
"""
import random
from time import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay: First argument

    Returns:
        float sleep
    """
    delay = random.uniform(0, max_delay)
    sleep(delay)
    return delay
