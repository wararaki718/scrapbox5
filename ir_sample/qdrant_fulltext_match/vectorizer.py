from typing import List

import numpy as np


class RandomVectorizer:
    def __init__(self):
        pass
    
    def generate(self, batch_size: int = 32, dimension: int = 768) -> List[List[float]]:
        vectors = np.random.random(size=(batch_size, dimension)).tolist()
        return vectors
