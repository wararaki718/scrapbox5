from pathlib import Path
from typing import Generator

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class CustomIterator:
    def __init__(self, data_directory: Path) -> Generator:
        self._data_directory = data_directory
    
    def __iter__(self) -> Generator[str, None, None]:
        for filepath in self._data_directory.iterdir():
            df = pd.read_csv(filepath)
            for row in df.itertuples():
                if len(row.token) % 2 == 0:
                    continue
                yield str(row.token)


def main() -> None:
    data_directory = Path("data")
    custom_iterator = CustomIterator(data_directory)

    for user_id in custom_iterator:
        print(user_id)
    
    vectorizer = CountVectorizer()
    vectorizer.fit(custom_iterator)
    print(vectorizer.get_feature_names_out())
    print("DONE")


if __name__ == "__main__":
    main()
