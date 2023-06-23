from pathlib import Path

from extractor import RuleExtractor
from evaluator import NEREvaluator
from loader import EntityLoader, CompanyLoader
from preprocessor import NERPreprocessor


def main() -> None:
    filepath = Path("ner.json")
    entity_loader = EntityLoader()
    entities = entity_loader.load(filepath)
    print(f"entity loaded: {len(entities)}")

    preprocessor = NERPreprocessor()
    preprocessed_entites = preprocessor.transform(entities)
    print(f"preprocessed: {len(preprocessed_entites)}")
    # print(preprocessed_entites[0].tokens[0].part_of_speech())

    filepath = Path("14_kanagawa_all_20230531.csv")
    company_loader = CompanyLoader()
    companies = company_loader.load(filepath)
    print(f"company loaded: {len(companies)}")

    extractor = RuleExtractor()
    predictions = extractor.extract(preprocessed_entites)
    print(f"extracted")

    evaluator = NEREvaluator()
    results = evaluator.evaluate(preprocessed_entites, predictions)
    print(results)

    print("DONE")


if __name__ == "__main__":
    main()
