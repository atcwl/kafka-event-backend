from app.core.logging import logger

async def handle_llm_result(result: dict):
    logger.info(f"✔ LLM task processed: {result}")

    # TODO: save to DB or emit to another topic
    # For now, log only.
