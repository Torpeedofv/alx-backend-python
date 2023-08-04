#!/usr/bin/env python3
"""A module for a type annotated function"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """A type annotated function that can return either of two types"""
    if key in dct:
        return dct[key]
    else:
        return default
