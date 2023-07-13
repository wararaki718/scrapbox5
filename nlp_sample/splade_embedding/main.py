from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np
import torch
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer

from builder import IndexBuilder
from retriever import IndexRetriever
from vectorizers import DocumentVectorizer, QueryVectorizer


def show(indices: List[int], id2vocab: Dict[int, str]) -> None:
    for index in indices:
        print(id2vocab[index])
    print()


def create_index(rows: List[torch.Tensor], cols: List[torch.Tensor], data: List[float], n_docs: int) -> Tuple[Dict[int, int], Dict[int, float]]:
    """
    rows: document id
    cols: vocabulary id # bert dictionary
    data: weight
    """
    index2docid = defaultdict(list)
    index2docvalue = defaultdict(list)
    for docid, dimid, value in zip(rows, cols, data):
        index2docid[dimid].append(docid)
        index2docvalue[dimid].append(value)
    return index2docid, index2docvalue
        

def retrieve(index2docid: Dict[int, int], index2docvalue: Dict[int, float], cols: List[int], values: List[float], threshold: float=0.) -> Tuple[List[int], List[float]]:
    scores = np.zeros(len(index2docid), np.float32)
    n = len(cols)
    for i in range(n):
        query_index = cols[i]
        x_query = values[i]
        doc_indices = index2docid[query_index]
        x_docs = index2docvalue[query_index]
        for index, x_doc in zip(doc_indices, x_docs):
            scores[index] += x_query * x_doc
        
    results = np.argwhere(scores > threshold)[:, 0]
    return results, scores[results]


def select_topk(indices: List[int], scores: List[float], top_k: int=1) -> Tuple[List[int], List[float]]:
    new_indices = np.argpartition(scores, top_k)[::-1][:top_k]
    indices = indices[new_indices]
    scores = scores[new_indices]
    return indices, scores


def main() -> None:
    model_name = "naver/splade-cocondenser-selfdistil"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    id2vocab = {v: k for k, v in tokenizer.vocab.items()}

    model = Splade(model_name, agg="max")
    model.eval()

    ids = [1, 2]
    texts = [
        "This is an apple. The apple is red.",
        "This is an orange. The orange is orange"
    ]
    queries = [
        "berry red",
        "mango yellow"
    ]

    model.eval()
    with torch.no_grad():
        tokens = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=500)
        document_embeddings = model(d_kwargs=tokens)
        rows, columns = torch.nonzero(document_embeddings["d_rep"], as_tuple=True)
        print(document_embeddings.keys())
        print(document_embeddings["d_rep"].shape)
        print(document_embeddings["d_rep"].squeeze().shape)
        print(document_embeddings["d_rep"][rows, columns].shape)
        print()
        # show(columns.squeeze().cpu().tolist(), id2vocab)
        data = document_embeddings["d_rep"][rows, columns].tolist()

        # row, col, data, len(ids)
        index2docid, index2docvalue = create_index(rows.tolist(), columns.tolist(), data, len(ids))
        print(index2docid)
        print()
        print(index2docvalue)
        print()

        tokens = tokenizer(queries, padding=True, truncation=True, return_tensors="pt", max_length=500)
        query_embeddings = model(q_kwargs=tokens)
        rows, columns = torch.nonzero(query_embeddings["q_rep"], as_tuple=True)
        print(query_embeddings.keys())
        print(query_embeddings["q_rep"].shape)
        print(query_embeddings["q_rep"].squeeze().shape) # the dimension is the number of vocabs
        print()

        data = query_embeddings["q_rep"][rows, columns].tolist()
        results, scores = retrieve(index2docid, index2docvalue, columns.tolist(), data)
        print(results)
        print()
        print(scores)
        print()

        results, scores = select_topk(results, scores)
        print(results)
        print()
        print(scores)
        print("#########")

    # modules
    document_vectorizer = DocumentVectorizer(model, tokenizer)
    query_vectorizer = QueryVectorizer(model, tokenizer)
    retriever = IndexRetriever()
    
    document_ids, vocab_ids, values = document_vectorizer.vectorize(texts)
    index = IndexBuilder.build(document_ids, vocab_ids, values)
    #print(index)

    vocab_ids, values = query_vectorizer.vectorize(queries)
    ids, scores = retriever.retrieve(index, vocab_ids, values)
    print(ids)
    print()
    print(scores)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
