import os

os.environ["DATABASE_URL"] = "sqlite:///./test.db"


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_index_page():
    response = client.get("/index")
    assert response.status_code == 200
