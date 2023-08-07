#!/usr/bin/env python3
"""A module for an asynchronous coroutine"""
import asyncio
from typing import Union
import random


async def wait_random(max_delay: Union[int, float]  =10) -> float:
    """A type annotated asynchronous coroutine that takes in an integer argument
    and returns a float"""i =  random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i 
