from pathlib import Path
from typing import Generator

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class CustomFilter:
    def __call__(self, text: str) -> bool:
        return len(text) % 2 == 1


class CustomIterator:
    def __init__(self, data_directory: Path) -> None:
        self._data_directory = data_directory
        self._custom_filter = CustomFilter()
    
    def __iter__(self) -> Generator[str, None, None]:
        for filepath in self._data_directory.iterdir():
            df = pd.read_csv(filepath)
            for token in filter(self._custom_filter, df.token):
                yield token


def main() -> None:
    data_directory = Path("sample")
    custom_iterator = CustomIterator(data_directory)

    for user_id in custom_iterator:
        print(user_id)
    
    vectorizer = CountVectorizer()
    vectorizer.fit(custom_iterator)
    print(vectorizer.get_feature_names_out())
    print("DONE")


if __name__ == "__main__":
    main()
