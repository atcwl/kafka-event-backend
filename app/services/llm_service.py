from app.services.llm_factory import get_llm

async def run_llm(provider: str, model: str, prompt: str) -> str:
    llm = get_llm(provider, model)
    out = await llm.ainvoke(prompt)
    return out.content
