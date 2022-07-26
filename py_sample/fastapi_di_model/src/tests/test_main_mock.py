from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from api.main import app, get_model


@pytest.fixture
def client() -> TestClient:
    api = TestClient(app)
    model_mock = MagicMock()
    model_mock.predict = MagicMock(return_value=2)
    
    app.dependency_overrides[get_model] = lambda: model_mock
    yield api
    app.dependency_overrides = dict()


def test_predict_mock(client: TestClient):
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"value": 2}
