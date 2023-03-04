from pathlib import Path
from typing import Any

import joblib

#from ..vectorizer import TitanicVectorizer


class VectorizerDumper:
    def __init__(self):
        pass

    def dump(self, vectorizer: Any, vectorizer_path: Path):
        joblib.dump(vectorizer._embarked_vectorizer._vectorizer, vectorizer_path)
