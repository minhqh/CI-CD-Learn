from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD Pipeline!"}

def test_process_data_valid():
    # Test với ID chẵn (Kỳ vọng: success)
    response = client.get("/process/42")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_process_data_invalid():
    # Test với ID lẻ (Kỳ vọng: error)
    response = client.get("/process/13")
    assert response.status_code == 200
    assert response.json()["status"] == "error"