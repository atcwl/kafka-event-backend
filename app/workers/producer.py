import uuid
from aiokafka import AIOKafkaProducer
from app.core.config import settings
from app.core.logging import logger

async def publish_task(text: str) -> str:
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP)
    await producer.start()

    try:
        request_id = str(uuid.uuid4())
        message = {"id": request_id, "text": text}
        await producer.send_and_wait(
            settings.REQUEST_TOPIC,
            str(message).encode("utf-8")
        )
        logger.info(f"Published message {request_id}")
        return request_id

    finally:
        await producer.stop()
