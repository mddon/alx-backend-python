#!/usr/bin/env python3
"""a python module to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function to execute async_comprehension 4 times
    Arguments:
        none
    Returns:
        the total execution time required to complete the task
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for k in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return (end_time - start_time)
