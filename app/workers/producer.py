import json
from app.core.kafka_util import init_producer
from app.core.logging import logger

async def send_to_kafka(topic: str, data: dict):
    producer = await init_producer()
    await producer.send_and_wait(topic, json.dumps(data).encode())
    logger.info(f"Sent event to topic={topic}: {data}")
