from typing import List


class QueryBuilder:
    @classmethod
    def build(cls, vector: List[float], size: int=5, k: int=5) -> dict:
        query = {
            "size": size,
            "query": {
                "knn": {
                    "vector": {
                        "vector": vector,
                        "k": k
                    }
                }
            }
        }
        return query
