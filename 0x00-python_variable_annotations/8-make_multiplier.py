#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type annotated function that takes a float as argument and returns
    a function that multiplies a float by the first argument"""
    return lambda x : x * multiplier
