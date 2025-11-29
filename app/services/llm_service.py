import openai
from app.core.config import settings
from app.core.logging import logger

openai.api_key = settings.OPENAI_API_KEY

async def run_llm_inference(text: str) -> dict:
    """
    Calls OpenAI GPT model to summarize or analyze input text.
    """

    logger.info(f"Sending text to OpenAI: {text}")

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": f"Process this text: {text}"}
            ],
            temperature=0.2
        )

        result = response.choices[0].message["content"]

        logger.info(f"OpenAI response: {result}")

        return {
            "input": text,
            "llm_output": result
        }

    except Exception as e:
        logger.error(f"OpenAI LLM error: {e}")
        raise
