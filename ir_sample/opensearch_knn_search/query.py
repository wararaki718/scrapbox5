class QueryBuilder:
    @classmethod
    def build(cls) -> dict:
        query = {
            "size": 2,
            "query": {
                "knn": {
                    "vector": {
                        "vector": [2, 3, 5, 6],
                        "k": 2
                    }
                }
            }
        }
        return query
