from collections import defaultdict
from typing import Dict, List, Optional

from document import Document


class IndexBuilder:
    @classmethod
    def build(
        cls, 
        document_ids: List[int],
        vocab_ids: List[int],
        values: List[float],
        n_docs: Optional[int] = None
    ) -> Dict[int, List[Document]]:
        index = defaultdict(list)
        for document_id, vocab_id, value in zip(document_ids, vocab_ids, values):
            document = Document(document_id=document_id, value=value)
            index[vocab_id].append(document)
        return index
