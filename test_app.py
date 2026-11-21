import pytest
from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config.update({"TESTING": True})
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_message(client):
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "CI/CD and Docker Pipeline is a massive success! V2"
    assert data["version"] == "2.0"


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
