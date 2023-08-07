#!/usr/bin/env python3
"""A module for a type annotated async function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Accepts two int as arguments and returns a float"""
    delay_list = [wait_random(max_delay) for i in range(n)]
    return await asyncio.gather(*delay_list)
