import os

class Settings:
    KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    REQUEST_TOPIC = "llm.requests"
    RESPONSE_TOPIC = "llm.responses"

settings = Settings()
