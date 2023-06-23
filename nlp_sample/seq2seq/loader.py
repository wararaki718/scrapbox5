from typing import List

import numpy as np
import torch
from torch.utils.data import DataLoader, RandomSampler, TensorDataset

from schema.enum import TOKEN
from schema.lang import Lang
from schema.pair import Pair


MAX_LENGTH=10


class DataLoaderFactory:
    @classmethod
    def create(cls, input_lang: Lang, output_lang: Lang, pairs: List[Pair], batch_size: int=32) -> DataLoader:
        input_ids = np.zeros((len(pairs), MAX_LENGTH), dtype=np.int32)
        target_ids = np.zeros((len(pairs), MAX_LENGTH), dtype=np.int32)

        for i, pair in enumerate(pairs):
            i_ids = input_lang.get_ids(pair.input_)
            t_ids = output_lang.get_ids(pair.target)
            i_ids.append(TOKEN.EOS)
            t_ids.append(TOKEN.EOS)

            input_ids[i, :len(i_ids)] = i_ids
            target_ids[i, :len(t_ids)] = t_ids
        
        dataset = TensorDataset(
            torch.LongTensor(input_ids),
            torch.LongTensor(target_ids)
        )
        sampler = RandomSampler(dataset)
        dataloader = DataLoader(dataset, sampler=sampler, batch_size=batch_size)
        return dataloader
