#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A type annotated function that takes a string and an int
    or float as argument that returns a tuple"""
    return (k, v*v)
