import pandas as pd
import pytest

from project_template.batch.vectorizer import TitanicVectorizer


@pytest.fixture
def vectorizer() -> TitanicVectorizer:
    return TitanicVectorizer()


@pytest.fixture
def passengers() -> pd.DataFrame:
    data = [
        {"Pclass": 1, "Age": 11, "Embarked": "A", "Ages": 10},
        {"Pclass": 2, "Age": 11, "Embarked": "B", "Ages": 10}
    ]
    return pd.DataFrame(data)


def test_vectorize_passengers(vectorizer: TitanicVectorizer, passengers: pd.DataFrame):
    result = vectorizer.fit_transform(passengers)
    assert result.shape[0] == 2
    assert result.shape[1] == 5
