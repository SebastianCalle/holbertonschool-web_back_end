#!/usr/bin/env python3
"""
    Module with function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: str parameter
        Return:
            Callable
    """
    def multiplication(n: float) -> float:
        """
            Args:
                m: str parameter
                n: str parameter
            Return:
                float multiplication
        """
        return n * multiplier

    return multiplication
