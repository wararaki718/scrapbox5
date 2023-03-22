from pathlib import Path

import torch

from model import NNModel


class EmbeddingSaver:
    def __init__(self):
        pass

    def save(self, model: NNModel, model_path: Path):
        torch.save(model._embedding.state_dict(), model_path)
