from typing import List

from sentence import Sentence


class SentenceReader:
    def __init__(self):
        pass

    def read(self) -> List[Sentence]:
        items = [
            {"sentence": "hello world"},
            {"sentence": "hello world cup"},
            {"sentence": "hello goodbye"},
            {"sentence": "hello cup"},
            {"sentence": "world"},
        ]
        return [
            Sentence(sentence_id=i, **sentence) for i, sentence in enumerate(items)
        ]
