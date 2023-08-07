#!/usr/bin/env python3
"""A module for a function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Accepts two int as arguments and returns a float"""
    delay_list = [task_wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*delay_list))
