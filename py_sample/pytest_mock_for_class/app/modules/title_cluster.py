import joblib

class TitleCluster:
    def __init__(self, filepath: str):
        self._model = joblib.load(filepath)

    def transform(self, x: list):
        return x
