import pandas as pd
import pytest

from project_template.batch.vectorizer import TitanicVectorizer


@pytest.fixture
def vectorizer() -> TitanicVectorizer:
    return TitanicVectorizer()


def test_vectorize_passengers(vectorizer: TitanicVectorizer, passengers: pd.DataFrame):
    result = vectorizer.fit_transform(passengers)
    assert result.shape[0] == 2
    assert result.shape[1] == 5
