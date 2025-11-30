import asyncio
import math

async def retry_with_backoff(fn, retries=3, base_delay=1):
    last_error = None

    for attempt in range(retries):
        try:
            return await fn()
        except Exception as e:
            last_error = e
            delay = base_delay * math.pow(2, attempt)
            await asyncio.sleep(delay)

    raise last_error
