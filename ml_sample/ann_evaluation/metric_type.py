from enum import Enum

import faiss


class MetricType(Enum):
    L2: int = faiss.METRIC_L2
    IP: int = faiss.METRIC_INNER_PRODUCT # cos-sim
