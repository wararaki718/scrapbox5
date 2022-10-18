
import scipy.sparse as sps
from implicit.als import AlternatingLeastSquares



class UserVectorizer:
    def __init__(self, factors: int=32):
        self._factors = factors
        self._user_factors = None
    
    def fit_transform(self, x: sps.csr_matrix):
        model = AlternatingLeastSquares(factors=self._factors)
        model.fit(x)
        self._user_factors = model.user_factors
        return self._user_factors
