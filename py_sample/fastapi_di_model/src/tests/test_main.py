from functools import partial

import pytest
from fastapi.testclient import TestClient

from api.config import Config
from api.main import app, get_model
from api.model import Classifier


@pytest.fixture
def client() -> TestClient:
    api = TestClient(app)
    app.dependency_overrides[get_model] = partial(Classifier.get_model, Config(threshold=1))
    yield api
    app.dependency_overrides = {}


def test_predict_one(client: TestClient):
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"value": 1}


def test_predict_zero(client: TestClient):
    response = client.get("/0")
    assert response.status_code == 200
    assert response.json() == {"value": 0}
