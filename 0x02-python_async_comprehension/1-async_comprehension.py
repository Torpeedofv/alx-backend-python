#!/usr/bin/env python3
"""A module for a coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that returns 10 random numbers using async
    comprehensing on an imported function"""
    return [i async for i in async_generator()]
