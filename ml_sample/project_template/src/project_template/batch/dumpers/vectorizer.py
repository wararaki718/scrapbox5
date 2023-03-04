from pathlib import Path

import joblib

from project_template.batch.vectorizer import TitanicVectorizer


class VectorizerDumper:
    def __init__(self):
        pass

    def dump(self, vectorizer: TitanicVectorizer, vectorizer_path: Path):
        joblib.dump(vectorizer._embarked_vectorizer._vectorizer, vectorizer_path)
