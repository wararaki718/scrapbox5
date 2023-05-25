from transformers import T5Tokenizer, T5ForConditionalGeneration


def main():
    model_name = "doc2query/all-t5-base-v1"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

    input_ids = tokenizer.encode(
        text,
        max_length=384,
        truncation=True,
        return_tensors="pt"
    )
    outputs = model.generate(
        input_ids=input_ids,
        do_sample=True,
        top_p=0.95,
        num_return_sequences=5
    )
    print(type(outputs))
    print(outputs)

    print("Text:")
    print(text)

    print("Generated Queries:")
    for i, output in enumerate(outputs, start=1):
        query = tokenizer.decode(output, skip_special_tokens=True)
        print(f"{i}: {query}")
    
    print("DONE")


if __name__ == "__main__":
    main()
