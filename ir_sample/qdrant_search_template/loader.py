from typing import List, Generator

from schema.sentence import Sentence


class BatchLoader:
    def __init__(self) -> None:
        pass

    def load(self, sentences: List[Sentence], batch_size: int=32) -> Generator[List[Sentence], None, None]:
        for i in range(0, len(sentences), batch_size):
            yield sentences[i:i+batch_size]
