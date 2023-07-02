from models import SiameseNetwork, TransformerFactory


def main() -> None:
    output_type = "MLM"
    model_name = "distilbert-base-uncased"
    document_transformer = TransformerFactory.create(output_type, model_name)
    query_transformer = TransformerFactory.create(output_type, model_name)

    model = SiameseNetwork(query_transformer, document_transformer)
    print("DONE")


if __name__ == "__main__":
    main()
