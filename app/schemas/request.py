from pydantic import BaseModel

class ProcessRequest(BaseModel):
    provider: str
    model: str
    prompt: str
