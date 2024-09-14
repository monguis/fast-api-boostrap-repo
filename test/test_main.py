from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app instance

client = TestClient(app)

def test_read_example():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}