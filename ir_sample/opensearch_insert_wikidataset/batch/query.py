import json
from pathlib import Path
from typing import Optional

from vectorizer import BertVectorizer


class QueryBuilder:
    @classmethod
    def build(cls, query_template_path: Path, keyword: str, vectorizer: Optional[BertVectorizer]=None) -> dict:
        with open(query_template_path) as f:
            query = json.load(f)
        
        if vectorizer is not None and "knn" in query["query"]:
            vectors = vectorizer.transform([keyword])
            query["query"]["knn"]["vector"]["vector"] = vectors[0]
        else:
            query["query"]["match"]["text"] = keyword
        return query
