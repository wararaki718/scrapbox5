from typing import List, Tuple

import scipy.sparse as sps
from implicit.als import AlternatingLeastSquares


class UserRecommender:
    def __init__(self, factors: int=32):
        self._model =  AlternatingLeastSquares(factors=factors)
    
    def fit(self, x: sps.csr_matrix):
        self._model.fit(x)

    def recommend(self,
                  user_id: int,
                  user_items: sps.csr_matrix,
                  n: int=20) -> Tuple[List[int], List[float]]:
        return self._model.recommend(user_id, user_items, n)
