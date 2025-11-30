import json
import redis.asyncio as redis

from app.core.config import settings

class ResponseManager:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL, decode_responses=True)

    async def store(self, request_id: str, data: dict):
        await self.redis.setex(request_id, 300, json.dumps(data))  # 5 min TTL

    async def get(self, request_id: str):
        val = await self.redis.get(request_id)
        return json.loads(val) if val else None

response_manager = ResponseManager()
