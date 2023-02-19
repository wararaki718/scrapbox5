from typing import List

from api.schemas.response import News


class Postprocessor:
    def __init__(self):
        pass

    def transform(self, hits: List[dict]) -> List[News]:
        results = [
            News(
                docid=hit["_id"],
                newsid=hit["_source"]["newsid"],
                context=hit["_source"]["context"]
            )
            for hit in hits
        ]

        return results
