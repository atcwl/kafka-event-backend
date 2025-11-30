import asyncio
import json

from app.core.kafka_util import create_consumer
from app.services.response_manager import response_manager
from app.core.config import settings
from app.core.logging import logger

async def kafka_response_listener():
    consumer = await create_consumer(settings.RESPONSE_TOPIC, "backend-group")
    logger.info("Response consumer started.")

    while True:
        msg = await consumer.getone()
        data = json.loads(msg.value)

        logger.info(f"Backend received response: {data}")
        await response_manager.store(data["request_id"], data)
        logger.info(f"Stored response for request_id={data['request_id']}")
        