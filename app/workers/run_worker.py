import asyncio
from app.workers.consumer import consume_requests

if __name__ == "__main__":
    asyncio.run(consume_requests())
