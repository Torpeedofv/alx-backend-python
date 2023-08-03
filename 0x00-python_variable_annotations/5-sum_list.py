#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """A type annotated function that takes a list of floats
    as argument and returns their sum as a float"""
    return float(sum(input_list))
