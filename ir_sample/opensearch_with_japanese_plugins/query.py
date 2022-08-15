class QueryBuilder:
    @classmethod
    def build(cls, keyword: str, size: int=5) -> dict:
        query = {
            "size": size,
            "query": {
                "match_phrase": {
                    "context": keyword
                }
            }
        }
        return query
