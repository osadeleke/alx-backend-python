#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Complex types - functions
    """
    def inner_multiplier(multiplier: float) -> float:
        """
        Complex types - functions
        """
        return multiplier * multiplier
    return inner_multiplier
