import uuid
from fastapi import APIRouter, HTTPException

from app.schemas.request import ProcessRequest
from app.services.response_manager import response_manager
from app.workers.producer import send_to_kafka
from app.core.config import settings

router = APIRouter()

@router.post("/process")
async def process_event(req: ProcessRequest):
    request_id = str(uuid.uuid4())

    event = {
        "request_id": request_id,
        "provider": req.provider,
        "model": req.model,
        "prompt": req.prompt,
    }

    await send_to_kafka(settings.REQUEST_TOPIC, event)

    return {"request_id": request_id}

@router.get("/result/{request_id}")
async def get_result(request_id: str):
    data = await response_manager.get(request_id)
    if not data:
        raise HTTPException(404, "Result not ready or not found")
    return data
