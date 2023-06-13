import numpy as np
import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer


def main() -> None:
    text = "Organgutans are native to the rainforests of Indonesia and Malaysia"

    model_name = "naver/splade-cocondenser-ensembledistil"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)

    tokens = tokenizer(text, return_tensors="pt")
    output = model(**tokens)
    print(output)
    print(output.logits.shape)
    print()

    vectors = torch.max(
        torch.log(1 + torch.relu(output.logits)) * tokens.attention_mask.unsqueeze(-1), dim=1
    )[0].squeeze()
    print(vectors)
    print(vectors.shape)
    print()

    columns = vectors.nonzero().squeeze().cpu().tolist()
    print(len(columns))
    print()

    weights = vectors[columns].cpu().tolist()
    sparse_dict = dict(zip(columns, weights))
    print(sparse_dict)
    print()

    idx2token = {
        index: token for token, index in tokenizer.get_vocab().items()
    }
    sparse_dict_tokens = {
        idx2token[index]: round(weight, 2) for index, weight in zip(columns, weights)
    }
    print(sparse_dict_tokens)
    print()

    texts = [
        "Programmed cell death (PCD) is the regulated death of cells within an organism",
        "How is the scheduled death of cells within a living thing regulated?",
        "Photosynthesis is the process of storing light energy as chemical energy in cells"
    ]

    tokens = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True
    )
    output = model(**tokens)
    vectors = torch.max(
        torch.log(1 + torch.relu(output.logits)) * tokens.attention_mask.unsqueeze(-1),
        dim=1
    )[0].squeeze().detach().cpu().numpy()
    print(vectors.shape)
    print()

    similarity = np.zeros((vectors.shape[0], vectors.shape[0]))
    for i, vector in enumerate(vectors):
        similarity[i,:] = np.dot(vector, vectors.T) / (np.linalg.norm(vector) * np.linalg.norm(vectors, axis=1))
    print(similarity)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
