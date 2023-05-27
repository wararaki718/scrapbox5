import spacy
from transformers import BertJapaneseTokenizer, BertForTokenClassification, pipeline

def main():
    text = "私は東京の会社でカレーを食べます。100円でした。"
    print(f"text: {text}")
    print()

    print("spacy:")
    nlp = spacy.load("ja_core_news_sm")
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print()

    print("transformers:")
    model = BertForTokenClassification.from_pretrained("jurabi/bert-ner-japanese")
    tokenizer = BertJapaneseTokenizer.from_pretrained("jurabi/bert-ner-japanese")

    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)
    results = ner_pipeline(text)
    for result in results:
        print(result)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
