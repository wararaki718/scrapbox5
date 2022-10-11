from typing import List, Tuple

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def ranking(query_vector: np.ndarray, document_vectors: np.ndarray, topn: int=100) -> List[Tuple[int, float]]:
    similarities = cosine_similarity(query_vector, document_vectors)
    indices = np.argsort(similarities)[0, -topn:]
    results = [
        (index, similarities[0, index]) for index in indices
    ]
    return results[::-1]


if __name__ == "__main__":
    from utils import get_data
    query = get_data(1, 4)
    documents = get_data(10, 4)
    print(query)
    print()
    print(documents)
    print()

    results = ranking(query, documents, topn=5)
    print(results)
