import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    REQUEST_TOPIC = "llm.requests"
    RESPONSE_TOPIC = "llm.responses"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
