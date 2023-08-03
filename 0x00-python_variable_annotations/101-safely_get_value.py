#!/usr/bin/env python3
"""A module for a type annotated function"""


def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
