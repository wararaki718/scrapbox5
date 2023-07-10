from typing import Generator
from unittest.mock import patch, MagicMock

import numpy as np
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    predictor = MagicMock()
    predictor.predict = MagicMock(return_value=np.array([[0]]))
    with patch("project_template.predictor.Predictor", return_value=predictor):
        ## TODO refactor
        from project_template.main import app
        yield TestClient(app)


def test_ping(client: TestClient) -> None:
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"


def test_predict(client: TestClient) -> None:
    body = {
        "Pclass": 1,
        "Age": 10,
        "Embarked": "C"
    }
    response = client.post("/predict", json=body)
    assert response.status_code == 200
    assert response.json()["survived"] == 0
