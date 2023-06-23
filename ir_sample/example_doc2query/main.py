from query import QueryGenerator


def main() -> None:
    model_name = "doc2query/msmarco-japanese-mt5-base-v1"
    generator = QueryGenerator(model_name)

    text = "東京ごご飯を食べます。"
    results = generator.generate(text)
    print(results)
    
    print("DONE")


if __name__ == "__main__":
    main()
