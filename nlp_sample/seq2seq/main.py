from pathlib import Path

from preprocessor import Preprocessor
from reader import LangReader


def main() -> None:
    reader = LangReader()
    filename = Path("jpn.txt")
    input_lang, output_lang, pairs = reader.read(filename, "en", "ja")
    print(f"number of pairs: {len(pairs)}")

    preprocessor = Preprocessor()
    input_lang, output_lang, pairs = preprocessor.transform(input_lang, output_lang, pairs)
    print("number of words:")
    print(f"{input_lang.name}: {input_lang.n_words}")
    print(f"{output_lang.name}: {output_lang.n_words}")
    print()
    
    print("DONE")


if __name__ == "__main__":
    main()
