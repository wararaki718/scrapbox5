from typing import List, Tuple

import torch
import torch.nn as nn

from schema.enum import TOKEN
from schema.lang import Lang
from utils import try_gpu


class Seq2SeqEvaluator:
    def __init__(self) -> None:
        pass

    def evaluate(self,
                 encoder: nn.Module,
                 decoder: nn.Module,
                 sentence: str,
                 input_lang: Lang,
                 output_lang: Lang) -> Tuple[List[str], torch.Tensor]:
        encoder.eval()
        decoder.eval()
        with torch.no_grad():
            x = input_lang.get_tensor(sentence)
            x = try_gpu(x)

            encoder_outputs, encoder_hidden = encoder(x)
            decoder_outputs, _, decoder_attention = decoder(encoder_outputs, encoder_hidden)

            _, topk = decoder_outputs.topk(1)
            decoded_ids = topk.squeeze()

            decoded_words = []
            for i in decoded_ids:
                if i.item() == TOKEN.EOS:
                    decoded_words.append("<EOS>")
                    break
                decoded_words.append(
                    output_lang.index2word.get(i.item(), "")
                )
            
        return decoded_words, decoder_attention
