from py._path.local import LocalPath
from pathlib import Path

import pytest


@pytest.fixture
def titanic_path(tmp_path: LocalPath) -> Path:
    csv_path = Path(tmp_path) / "titanic.csv"
    csv_path.write_text("Pclass,Age,Embarked,Survived\n1,20,S,1")
    return csv_path
