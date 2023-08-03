#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type annotated function that takes a A list as argument
    and returns a float"""
    return float(sum(mxd_lst))
