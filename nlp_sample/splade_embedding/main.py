from collections import defaultdict
from typing import Dict, List, Tuple

import torch
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer


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

        query_embedding = model(q_kwargs=tokens)
        print(query_embedding.keys())
        print(query_embedding["q_rep"].shape)
        print(query_embedding["q_rep"].squeeze().shape) # the dimension is the number of vocabs
    print("DONE")


if __name__ == "__main__":
    main()
