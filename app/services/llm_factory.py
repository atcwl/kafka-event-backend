from groq import Groq
from openai import OpenAI
from app.core.config import settings

def create_llm(provider: str, model: str):
    if provider == "groq":
        client = Groq(api_key=settings.GROQ_API_KEY)

        async def run(prompt: str):
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return resp.choices[0].message.content

        return run

    if provider == "openai":
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        async def run(prompt: str):
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return resp.choices[0].message.content

        return run

    raise ValueError(f"Unknown provider: {provider}")
