import json
from aiokafka import AIOKafkaConsumer
from app.core.config import settings
from app.core.kafka_util import wait_for_kafka


async def create_consumer(topic: str):
    await wait_for_kafka(settings.KAFKA_BOOTSTRAP_SERVERS)

    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id=settings.KAFKA_GROUP_ID,
        auto_offset_reset="earliest",
    )
    await consumer.start()
    return consumer

