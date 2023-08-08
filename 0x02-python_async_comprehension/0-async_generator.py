#!/usr/bin/env python3
"""A module for a function"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that loops 10 times asynchronously and waits 1
    second each time and yields a number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
