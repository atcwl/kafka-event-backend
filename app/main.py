from fastapi import FastAPI
import asyncio

from app.api.routes import router
from app.core.response_consumer import kafka_response_listener

app = FastAPI()

@app.on_event("startup")
async def startup():
    asyncio.create_task(kafka_response_listener())

app.include_router(router)
