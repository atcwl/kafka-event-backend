from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Kafka LLM Backend")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Kafka LLM Backend Running"}
