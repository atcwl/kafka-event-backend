import ast
from aiokafka import AIOKafkaConsumer
from app.core.config import settings
from app.core.logging import logger

from app.services.llm_service import run_llm_inference
from app.services.process_event import handle_llm_result

async def consume_requests():
    consumer = AIOKafkaConsumer(
        settings.REQUEST_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP,
        group_id="llm-worker-group"
    )

    await consumer.start()
    logger.info("📥 LLM Worker listening for messages...")

    try:
        async for msg in consumer:
            payload = ast.literal_eval(msg.value.decode("utf-8"))
            logger.info(f"📨 Received message: {payload}")

            # Run LLM
            result = await run_llm_inference(payload["text"])

            # Process the result
            await handle_llm_result(result)

    finally:
        await consumer.stop()
        logger.info("🛑 Worker stopped.")
