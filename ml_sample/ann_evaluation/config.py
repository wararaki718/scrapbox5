from dataclasses import dataclass, asdict

from metric_type import MetricType


@dataclass
class ANNConfig:
    n_nearest_neigbhors: int = 32
    n_dimensions: int = 256
    metric_type: MetricType = MetricType.L2

    def to_dict(self) -> dict:
        return asdict(self)
