import random
from pathlib import Path

from evaluator import Seq2SeqEvaluator
from loader import DataLoaderFactory
from model import AttentionDecoder, Encoder
from preprocessor import Preprocessor
from reader import LangReader
from trainer import Seq2SeqTrainer
from utils import try_gpu


def main() -> None:
    reader = LangReader()
    filename = Path("data/eng-fra.txt")
    input_lang, output_lang, pairs = reader.read(filename, "eng", "fra", True)
    print(f"number of pairs: {len(pairs)}")

    preprocessor = Preprocessor()
    input_lang, output_lang, pairs = preprocessor.transform(input_lang, output_lang, pairs)
    print("number of words:")
    print(f"- {input_lang.name}: {input_lang.n_words}")
    print(f"- {output_lang.name}: {output_lang.n_words}")
    print()

    dataloader = DataLoaderFactory.create(input_lang, output_lang, pairs, 32)

    n_hidden = 128
    encoder = try_gpu(Encoder(input_lang.n_words, n_hidden))
    decoder = try_gpu(AttentionDecoder(n_hidden, output_lang.n_words))

    print("train:")
    trainer = Seq2SeqTrainer()
    trainer.train(dataloader, encoder, decoder, n_epochs=10, print_every=5)

    print("evaluate:")
    n = 10
    evaluator = Seq2SeqEvaluator()
    for _ in range(n):
        pair = random.choice(pairs)
        print(f"> {pair.input_}")
        print(f"= {pair.target}")
        output_words, _ = evaluator.evaluate(encoder, decoder, pair.input_, input_lang, output_lang)
        output_sentence = " ".join(output_words)
        print(f"< {output_sentence}")
        print()
    
    print("DONE")


if __name__ == "__main__":
    main()
