import asyncio
import socket
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from app.core.config import settings
from app.core.logging import logger

producer = None

async def wait_for_kafka(host: str, port: int, retries=20, delay=3):
    for attempt in range(1, retries + 1):
        logger.info(f"Connecting to Kafka at {host}:{port} (attempt {attempt})")
        try:
            socket.create_connection((host, port), timeout=2).close()
            logger.info("Kafka is ready.")
            return True
        except:
            logger.warning(f"Kafka not ready. Retry {attempt}/{retries}")
            await asyncio.sleep(delay)
    raise RuntimeError("Kafka failed to start")

async def init_producer():
    global producer
    if producer:
        return producer

    host, port = settings.KAFKA_BOOTSTRAP_SERVERS.split(":")
    await wait_for_kafka(host, int(port))

    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
    )
    await producer.start()
    logger.info("Kafka producer started.")
    return producer

async def create_consumer(topic: str, group_id: str):
    host, port = settings.KAFKA_BOOTSTRAP_SERVERS.split(":")
    await wait_for_kafka(host, int(port))

    consumer = AIOKafkaConsumer(
        topic,
        group_id=group_id,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
    )
    await consumer.start()
    logger.info(f"Kafka consumer started for topic={topic}")
    return consumer
