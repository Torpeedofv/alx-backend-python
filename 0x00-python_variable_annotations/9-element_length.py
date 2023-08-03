#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that accepts a list as argument and returns a list"""
    return [(i, len(i)) for i in lst]
