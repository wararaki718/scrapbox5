import pandas as pd
import pytest


@pytest.fixture
def full_columns_data() -> pd.DataFrame:
    data = [{
        "PassengerId": 1,
        "Survived": 0,
        "Pclass": 1,
        "Name": "test",
        "Sex": "male",
        "Age": 10,
        "SibSp": 1,
        "Parch": 0,
        "Ticket": "ticket",
        "Fare": 7.25,
        "Cabin": "C85",
        "Embarked": "C"
    }]
    return pd.DataFrame(data)


@pytest.fixture
def missing_pclass_cell_data() -> pd.DataFrame:
    data = [
        {"Pclass": 1, "Age": 10, "Embarked": "C", "Survived": 1},
        {"Age": 10, "Embarked": "C", "Survived": 1},
    ]
    return pd.DataFrame(data)


@pytest.fixture
def missing_age_cell_data() -> pd.DataFrame:
    data = [
        {"Pclass": 1, "Age": 10, "Embarked": "C", "Survived": 1},
        {"Pclass": 1, "Embarked": "C", "Survived": 1},
    ]
    return pd.DataFrame(data)


@pytest.fixture
def missing_embarked_cell_data() -> pd.DataFrame:
    data = [
        {"Pclass": 1, "Age": 10, "Embarked": "C", "Survived": 1},
        {"Pclass": 1, "Age": 10, "Survived": 1},
    ]
    return pd.DataFrame(data)
