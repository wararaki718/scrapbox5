import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from analyzer import TextAnalyzer


class TextVectorizer:
    def __init__(self):
        analyzer = TextAnalyzer()
        self._tfidf = TfidfVectorizer(tokenizer=analyzer.analyze)
    
    def fit_transform(self, sentences: pd.Series) -> np.ndarray:
        return self._tfidf.fit_transform(sentences)
