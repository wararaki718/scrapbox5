from typing import List, Tuple

import scipy.sparse as sps
from implicit.als import AlternatingLeastSquares


class ItemRecommender:
    def __init__(self, factors: int=32):
        self._model =  AlternatingLeastSquares(factors=factors)
    
    def fit(self, x: sps.csr_matrix):
        self._model.fit(x)

    def recommend(self,
                  item_id: int,
                  n: int=20) -> Tuple[List[int], List[float]]:
        return self._model.similar_items(item_id, N=n, filter_items=[item_id])
