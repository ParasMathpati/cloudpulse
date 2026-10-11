from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_dashboard():
    response = client.get("/")
    assert response.status_code == 200
    assert "CloudPulse" in response.text

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_readiness():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "cloudpulse_http_requests_total" in response.text
