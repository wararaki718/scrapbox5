import random
from typing import Optional, Tuple

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision.datasets import ImageFolder
from torchvision.transforms import Compose


class SiameseNetworkDataset(Dataset):
    def __init__(self, image_dataset: ImageFolder, transform: Optional[Compose] = None) -> None:
        self._image_dataset = image_dataset
        if transform is not None:
            self._transform = transform
        else:
            self._transform = lambda x: x
    
    def __getitem__(self, index: int) -> Tuple[Image.Image, Image.Image, torch.Tensor]:
        data0: Tuple[str, int] = random.choice(self._image_dataset.imgs)

        is_same_class = random.randint(0, 1)
        if is_same_class:
            while True:
                data1 = random.choice(self._image_dataset.imgs)
                if data0[1] == data1[1]:
                    break
        else:
            while True:
                data1 = random.choice(self._image_dataset.imgs)
                if data0[1] != data1[1]:
                    break
        
        img0 = Image.open(data0[0])
        img1 = Image.open(data1[0])

        img0 = img0.convert("L")
        img1 = img1.convert("L")

        img0: Image.Image = self._transform(img0)
        img1: Image.Image = self._transform(img1)

        label = torch.from_numpy(np.array([int(data0[1] != data1[1])], dtype=np.float32))

        return img0, img1, label

    def __len__(self) -> int:
        return len(self._image_dataset.imgs)
