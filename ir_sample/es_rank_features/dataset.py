from typing import Generator, List

from schema.doc import Document


class DatasetGenerator:
    @classmethod
    def generate(cls) -> Generator[Document, None, None]:
        docs: List[Document] = [
            Document(
                topics={"politics": 20, "economics": 50.8},
                negative_reviews={"1star":10, "2star":100}
            ),
            Document(
                topics={"politics": 5.2, "sports": 80.1},
                negative_reviews={"1star":1, "2star":10}
            )
        ]

        for doc in docs:
            yield doc
