from typing import List

from news import News
from vectorizer import NewsVectorizer


class NewsPreprocessor:
    def __init__(self, vectorizer: NewsVectorizer):
        self._vectorizer = vectorizer
    
    def transform(self, news: List[News]) -> List[News]:
        vectors = self._vectorizer.transform(news)
        for i in range(len(vectors)):
            news[i].vector = vectors[i]
        return news
