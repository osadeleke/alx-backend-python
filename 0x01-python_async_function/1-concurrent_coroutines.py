#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""

import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
  for n in range(n):
    await asyncio.run(wait_random(max_delay))
  return [1, 2, 3]