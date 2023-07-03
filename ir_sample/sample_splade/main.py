from models import SiameseNetwork, TransformerFactory, CustomTokenizer


def main() -> None:
    output_type = "MLM"
    model_name = "distilbert-base-uncased"
    tokenizer = CustomTokenizer(model_name)
    document_transformer = TransformerFactory.create(output_type, model_name)
    query_transformer = TransformerFactory.create(output_type, model_name)

    model = SiameseNetwork(query_transformer)
    print("DONE")


if __name__ == "__main__":
    main()
