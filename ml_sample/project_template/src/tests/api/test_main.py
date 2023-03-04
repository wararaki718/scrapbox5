# import pytest
# from fastapi.testclient import TestClient

# from project_template.api.main import app


# @pytest.fixture
# def client() -> TestClient:
#     return TestClient(app)



# def test_ping(client: TestClient) -> None:
#     response = client.get("/ping")
#     assert response.status_code == 200
#     assert response.json() == "pong"
