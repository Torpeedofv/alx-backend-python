#!/usr/bin/env python3
"""A module for a duck typed annotated function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that takes a list as arguments. The elements of the list
    is not known. The function returns a Either anything or nothing"""
    if lst:
        return lst[0]
    else:
        return None
