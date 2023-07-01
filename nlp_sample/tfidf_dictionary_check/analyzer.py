from typing import List


class CustomAnalyzer:
    def __init__(self) -> None:
        self._stopwords = ["is", "this"]
        self._dictionary = {"machine learning": "machine_learning"}

    def __call__(self, text: str) -> List[str]:
        for key, value in self._dictionary.items():
            text = text.replace(key, value)

        tokens = text.split()
        tokens = [token for token in tokens if token not in self._stopwords]
        return tokens
