from .modules import AgeCluster, TitleCluster


class ClusteringScorer:
    def __init__(self, config_path: str):
        self._age = AgeCluster(config_path)
        self._title = TitleCluster(config_path)

    def transform(self, x: list):
        x = self._age.transform(x)
        x = self._title.transform(x)
        return x
