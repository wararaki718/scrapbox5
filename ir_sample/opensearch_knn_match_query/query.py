from typing import List, Optional

class QueryBuilder:
    @classmethod
    def build(cls, keyword: Optional[str]=None, vector: Optional[List[float]]=None, size: int=5, k: int=5) -> dict:
        queries = []

        if keyword is not None:
            queries.append({
                "match_phrase": {
                    "context": keyword
                }
            })
        
        if vector is not None:
            queries.append({
                "knn": {
                    "vector": {
                        "vector": vector,
                        "k": k
                    }
                }
            })
        
        if len(queries) > 1:
            query = {
                "size": size,
                "query": {
                    "bool": {
                        "must": queries
                    }
                }
            }
        else:
            query = {
                "size": size,
                "query": queries[0]
            }
        return query
