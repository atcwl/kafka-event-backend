import asyncio

async def with_retry(task, retries=5, delay=1):
    for attempt in range(retries):
        try:
            return await task()
        except Exception:
            await asyncio.sleep(delay * (attempt + 1))
    raise Exception("Task failed after retries")
