from pathlib import Path

import pytest

from project_template.batch.loaders import TitanicLoader


@pytest.fixture
def loader() -> TitanicLoader:
    return TitanicLoader()


def test_load_titanic(titanic_path: Path, loader: TitanicLoader):
    df = loader.load(titanic_path)
    assert df.shape[0] == 1
