from typing import List

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

from analyzer import TextAnalyzer


class LDAVectorizer:
    def __init__(self, n_components: int = 128) -> None:
        analyzer = TextAnalyzer()
        self._count_vectorizer = CountVectorizer(analyzer=analyzer.analyze)
        self._lda = LatentDirichletAllocation(n_components=n_components)
    
    def fit_transform(self, texts: List[str]) -> np.ndarray:
        x = self._count_vectorizer.fit_transform(texts)
        x = self._lda.fit_transform(x)
        return x
