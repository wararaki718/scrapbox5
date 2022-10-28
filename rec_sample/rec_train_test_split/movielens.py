from pathlib import Path
from urllib.request import urlopen
from typing import Tuple
from zipfile import ZipFile

import pandas as pd


def _is_downloaded(download_path: Path = Path("./data/movielens.zip")) -> bool:
    filepath = download_path / "movielens.zip"
    return filepath.exists()


def _download_movielens(url: str,
             download_path: Path = Path("./data/movielens.zip")):
    download_path.parent.mkdir(exist_ok=True)
    with urlopen(url) as response, open(download_path, "wb") as f:
        f.write(response.read())


def _read_movielens(filepath: Path) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data = dict()
    with ZipFile(filepath) as zf:
        for filename in filter(lambda x: x.endswith(".csv"), zf.namelist()):
            with zf.open(filename) as f:
                key = Path(filename).stem
                value = pd.read_csv(f)
                data[key] = value
    
    return data["movies"], data["ratings"], data["tags"], data["links"]


def get_movielens(download_dir: Path = "./data") -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    download_path = download_dir / "movielens.zip"
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

    if not _is_downloaded(download_path):
        _download_movielens(url, download_path)
        print("movielens was downloaded!")
    
    movies, ratings, tags, links = _read_movielens(download_path)
    return movies, ratings, tags, links
