import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModel


class TransformerFactory:
    @classmethod
    def create(cls, output_type: str, model_name: str, fp16: bool=False) -> nn.Module:
        if output_type == "cls":
            return CLSTransformer(model_name, fp16)
        elif output_type == "hidden_states":
            return HiddenStatesTransformer(model_name, fp16)
        elif output_type == "mean":
            return MeanTransformer(model_name, fp16)
        elif output_type == "MLM": # MLM
            return MLMTransformer(model_name, fp16)
        else:
            raise RuntimeError


class CLSTransformer(nn.Module):
    def __init__(self, model_name: str, fp16: bool=False) -> None:
        super().__init__()
        self._model = AutoModel(model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._fp16 = fp16
    
    def forward(self, **tokens) -> torch.Tensor:
        with torch.cuda.amp.autocast():
            hiddens = self._model(**tokens)[0]
        out = hiddens[:, 0, :]
        return out


class HiddenStatesTransformer(nn.Module):
    def __init__(self, model_name: str, fp16: bool=False) -> None:
        super().__init__()
        self._model = AutoModel(model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._fp16 = fp16
    
    def forward(self, **tokens) -> tuple:
        with torch.cuda.amp.autocast():
            hiddens = self._model(**tokens)[0]
        return hiddens, tokens["attention_mask"]


class MeanTransformer(nn.Module):
    def __init__(self, model_name: str, fp16: bool=False) -> None:
        super().__init__()
        self._model = AutoModel(model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._fp16 = fp16
    
    def forward(self, **tokens) -> torch.Tensor:
        with torch.cuda.amp.autocast():
            hiddens = self._model(**tokens)[0]
        out = torch.sum(
            hiddens * tokens["attention_mask"].unsqueeze(-1),
            dim=1
        ) / torch.sum(tokens["attention_mask"], dim=-1, keepdim=True)
        return out


class MLMTransformer(nn.Module):
    def __init__(self, model_name: str, fp16: bool=False) -> None:
        super().__init__()
        self._model = AutoModelForMaskedLM.from_pretrained(model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._fp16 = fp16
    
    def forward(self, **tokens) -> torch.Tensor:
        with torch.cuda.amp.autocast():
            out = self._model(**tokens)
        return out
