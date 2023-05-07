import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def main():
    model_name = "doc2query/msmarco-japanese-mt5-base-v1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    text = "Python（パイソン）はインタープリタ型の高水準汎用プログラミング言語である。グイド・ヴァン・ロッサムにより創り出され、1991年に最初にリリースされたPythonの設計哲学は、有意なホワイトスペース(オフサイドルール)の顕著な使用によってコードの可読性を重視している。その言語構成とオブジェクト指向のアプローチは、プログラマが小規模なプロジェクトから大規模なプロジェクトまで、明確で論理的なコードを書くのを支援することを目的としている。"
    input_ids = tokenizer.encode(text, return_tensors="pt")

    with torch.no_grad():
        sampling_outputs = model.generate(
            input_ids=input_ids,
            max_length=64,
            do_sample=True,
            top_p=0.95,
            top_k=10,
            num_return_sequences=5
        )

        beam_outputs = model.generate(
            input_ids=input_ids, 
            max_length=64, 
            num_beams=5, 
            no_repeat_ngram_size=2, 
            num_return_sequences=5, 
            early_stopping=True
        )
    
    print("beam:")
    for i, output in enumerate(beam_outputs, start=1):
        query = tokenizer.decode(output, skip_special_tokens=True)
        print(f"{i}: {query}")
    print()
    
    print("sample:")
    for i, output in enumerate(sampling_outputs):
        query = tokenizer.decode(output, skip_special_tokens=True)
        print(f"{i}: {query}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
