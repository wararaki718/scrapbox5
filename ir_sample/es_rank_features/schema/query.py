from dataclasses import dataclass


@dataclass
class Query:
    rank_feature: str

    def to_query(self) -> dict:
        return {
            "query": {
                "rank_feature": {
                    "field": self.rank_feature
                }
            }
        }
