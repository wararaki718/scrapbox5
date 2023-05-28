import torch
from transformers import AutoTokenizer, AutoModel


def main():
    model_name = "BeIR/sparta-msmarco-distilbert-base-v1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    text = "This is an apple. The apple is red."
    
    model.eval()
    with torch.no_grad():
        tokens = tokenizer([text], padding=True, truncation=True, return_tensors="pt", max_length=500)
        embedding = model(**tokens).last_hidden_state.mean(1)
    
    print(embedding.shape)
    print("DONE")


if __name__ == "__main__":
    main()
