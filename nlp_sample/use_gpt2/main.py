import torch
from transformers import GPT2Tokenizer, GPT2Model


def main():
    # tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2Model.from_pretrained("gpt2")
    
    text = "hello, world"
    inputs = tokenizer(text, return_tensors="pt")
    print(inputs["input_ids"])

    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    print(embeddings)
    print(embeddings.shape)

    embeddings = torch.squeeze(embeddings)
    print(embeddings.shape)
    print("DONE")


if __name__ == "__main__":
    main()
