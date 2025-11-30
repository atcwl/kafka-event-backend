import asyncio
import json
import signal

from app.core.kafka_util import create_consumer
from app.workers.producer import send_to_kafka
from app.services.process_event import process_event
from app.core.config import settings
from app.core.logging import logger

stop_flag = False

def handle_stop(*_):
    global stop_flag
    stop_flag = True
    logger.info("Stopping worker...")

signal.signal(signal.SIGINT, handle_stop)
signal.signal(signal.SIGTERM, handle_stop)

async def worker_loop():
    consumer = await create_consumer(settings.REQUEST_TOPIC, "worker-group")

    logger.info("Worker started.")

    while not stop_flag:
        msg = await consumer.getone()
        event = json.loads(msg.value)
        logger.info(f"Worker got event: {event}")

        result = await process_event(event)
        result["request_id"] = event["request_id"]

        await send_to_kafka(settings.RESPONSE_TOPIC, result)
        logger.info("Worker sent response.")

    await consumer.stop()

if __name__ == "__main__":
    asyncio.run(worker_loop())
