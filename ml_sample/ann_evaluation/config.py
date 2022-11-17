from dataclasses import dataclass, asdict

from metric_type import MetricType


@dataclass
class ANNConfig:
    n_nearest_neigbhors: int = 32
    n_dimensions: int = 256
    ef_construction: int = 64
    ef_search: int = 32
    metric_type: MetricType = MetricType.L2

    def to_dict(self) -> dict:
        return asdict(self)
