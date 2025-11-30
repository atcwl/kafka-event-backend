import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

    REQUEST_TOPIC = "llm.requests"
    RESPONSE_TOPIC = "llm.responses"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
