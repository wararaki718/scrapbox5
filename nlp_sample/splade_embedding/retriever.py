from typing import Dict, List, Tuple

import numpy as np

from document import Document


class IndexRetriever:
    def __init__(self, threshold: float=0.) -> None:
        self._threshold = threshold
    
    def retrieve(self, index: Dict[int, List[Document]], vocab_ids: List[int], values: List[float], topk: int=10) -> Tuple[List[int], List[float]]:
        matrix = np.zeros(len(index), np.float32)
        for vocab_id, value in zip(vocab_ids, values):
            documents = index[vocab_id]
            for document in documents:
                matrix[document.document_id] += value * document.value
        
        # retrieve
        ids = np.argwhere(matrix > self._threshold)[:, 0]
        scores = matrix[ids]

        # ranking
        topk = min(topk, len(ids)-1)
        reranked_indices = np.argpartition(scores, topk)[::-1][:topk]
        ids = ids[reranked_indices]
        scores = scores[reranked_indices]

        return ids, scores
