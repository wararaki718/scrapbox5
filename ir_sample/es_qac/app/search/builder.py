class QueryBuilder:
    def __init__(self) -> None:
        pass

    @classmethod
    def build(self, keyword: str) -> dict:
        return {
            "size":0,
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "my_field.suggest": {
                                    "query": keyword
                                }
                            }
                        },
                        {
                            "match": {
                                "my_field.readingform": {
                                    "query": keyword,
                                    "fuzziness":"AUTO",
                                    "operator": "and"
                                }
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "keywords": {
                    "terms": {
                        "field": "my_field",
                        "order": {
                            "_count": "desc"
                        },
                        "size":"10"
                    }
                }
            }
        }
