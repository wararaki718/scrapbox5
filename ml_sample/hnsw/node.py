from dataclasses import dataclass
import numpy as np


@dataclass
class Node:
    data: np.ndarray
    friends: set
