from dataclasses import dataclass, field
from typing import List

from node import Node


@dataclass
class Layer:
    nodes: List[Node] = field(default_factory=list)
