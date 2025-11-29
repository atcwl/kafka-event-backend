from app.core.logging import logger

async def handle_llm_result(result: dict):
    logger.info(f"Processed LLM result: {result}")
    # Placeholder: Save to DB or continue pipeline
