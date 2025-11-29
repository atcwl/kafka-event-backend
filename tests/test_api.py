from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_endpoint():
    response = client.post("/process", json={"text": "hello"})
    assert response.status_code == 200
