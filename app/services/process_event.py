from app.services.llm_factory import create_llm
from app.core.logging import logger

async def process_event(event: dict) -> dict:
    request_id = event.get("request_id")
    provider = event.get("provider")
    model = event.get("model")
    prompt = event.get("prompt")

    llm = create_llm(provider, model)

    try:
        logger.info(f"Running LLM: provider={provider}, model={model}")
        output = await llm(prompt)

        return {
            "request_id": request_id,
            "output": output,
            "provider": provider,
            "model": model,
            "error": None
        }

    except Exception as e:
        logger.error(f"LLM error: {e}")
        return {
            "request_id": request_id,
            "provider": provider,
            "model": model,
            "error": str(e)
        }
