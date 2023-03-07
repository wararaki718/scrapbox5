# from typing import Generator
# from unittest.mock import patch, MagicMock

# import numpy as np
# import pytest
# from fastapi.testclient import TestClient

# from project_template.api.main import app


# @pytest.fixture
# def client() -> Generator[TestClient, None, None]:
#     model = MagicMock()
#     model.predict = MagicMock(return_value=np.array([[0]]))
#     vectorizer = MagicMock()
#     vectorizer.transform = MagicMock(return_value=np.array([0]))
#     with patch("project_template.api.estimator.estimator.joblib.load", return_value=model):
#         with patch("project_template.api.vectorizer.components.embarked.joblib.load", return_value=vectorizer):
#             yield TestClient(app)


# def test_ping(client: TestClient) -> None:
#     response = client.get("/ping")
#     assert response.status_code == 200
#     assert response.json() == "pong"
