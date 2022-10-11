from typing import List, Tuple

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


## mmr reranking
def mmr(query_vector: np.ndarray, document_vectors: np.ndarray, selected_documents: List[Tuple[int, float]], lambda_: float=1.0, topn: int=100) -> List[Tuple[int, float]]:
    query_document_similarities = cosine_similarity(document_vectors, query_vector)
    document_similarities = cosine_similarity(document_vectors)

    best_document_indices = [np.argmax(query_document_similarities)]
    candidates_indices = [document[0] for document in selected_documents if best_document_indices[0] != document[0]]

    for _ in range(min(topn-1, len(selected_documents)-1)):
        candidates_similarities = query_document_similarities[candidates_indices, :]
        target_similarities = np.max(
            document_similarities[candidates_indices][:, best_document_indices], axis=1
        )

        mmr = lambda_ * candidates_similarities - (1 - lambda_) * target_similarities.reshape(-1, 1)
        mmr_indices = candidates_indices[np.argmax(mmr)]
        best_document_indices.append(mmr_indices)
        candidates_indices.remove(mmr_indices)
    
    results = [
        (index, round(float(query_document_similarities.reshape(1, -1)[0][index]), 4))
        for index in best_document_indices
    ]
    results.sort(key=lambda x: x[1], reverse=True)
    return results
