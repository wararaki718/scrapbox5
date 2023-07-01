import logging

import torch.nn.functional as F
from torch.utils.data import DataLoader

from model import SiameseNetwork


logger = logging.getLogger(__name__)


class Tester:
    def __init__(self) -> None:
        pass

    def test(
        self,
        model: SiameseNetwork,
        loader: DataLoader,
    ) -> None:

        for (img0, img1, label) in loader:
            img0 = img0.cuda()
            img1 = img1.cuda()
            label = label.cuda()
            
            output1, output2 = model(img0, img1)

            distance = F.pairwise_distance(output1, output2)
            logger.info(f"distance: {distance}, label: {label}")
