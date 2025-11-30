from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process():
    r = client.post("/process", json={"prompt": "hello"})
    assert r.status_code == 200
