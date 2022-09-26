#!/usr/bin/env python3
"""
    Module with function make_multiplier
"""
from typing import Callable


def make_multiplier(m: float) -> Callable[[float], float]:
    """
        Args:
            m: str parameter
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
        return m * n

    return multiplication
