from fastapi import APIRouter
from app.schemas.request import LLMRequest
from app.workers.producer import publish_task

router = APIRouter()

@router.post("/process")
async def process_text(payload: LLMRequest):
    request_id = await publish_task(payload.text)
    return {"status": "queued", "request_id": request_id}
