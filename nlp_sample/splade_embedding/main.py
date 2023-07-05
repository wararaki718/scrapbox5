import torch
from splade.models.transformer_rep import Splade
from transformers import AutoTokenizer


def main() -> None:
    model_name = "naver/splade-cocondenser-selfdistil"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = Splade(model_name, agg="max")
    model.eval()

    text = "This is an apple. The apple is red."

    model.eval()
    with torch.no_grad():
        tokens = tokenizer([text], padding=True, truncation=True, return_tensors="pt", max_length=500)
        document_embedding = model(d_kwargs=tokens)
        print(document_embedding.keys())
        print(document_embedding["d_rep"].shape)
        print(document_embedding["d_rep"].squeeze().shape)

        query_embedding = model(q_kwargs=tokens)
        print(query_embedding.keys())
        print(query_embedding["q_rep"].shape)
        print(query_embedding["q_rep"].squeeze().shape) # the dimension is the number of vocabs

    print("DONE")


if __name__ == "__main__":
    main()
