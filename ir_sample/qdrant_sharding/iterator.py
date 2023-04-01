from typing import Generator, List


class TextIterator:
    def __init__(self, texts: List[str], chunksize: int=128):
        self._texts = texts
        self._chunksize = chunksize

    def __iter__(self) -> Generator[List[str], None, None]:
        for i in range(0, len(self._texts), self._chunksize):
            yield self._texts[i: i+self._chunksize]
