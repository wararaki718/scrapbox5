import numpy as np

from insert import insert


class HNSW:
    def __init__(self, data: np.ndarray, m: int, m_max: int, ef: int, ml: int):
        """
        data: data
        m: number of established connections
        m_max: maximum number of connections for each element per layer
        ef: size of the dynamic candidate list
        ml: normalization factor for level generation
        """
        self._data = data
        self._layers = []
        self._n_established_connections = m
        self._max_num_connections = m_max
        self._n_candidates = ef
        self._norm_factor = ml
        self._ep = None
        self._ep_level = None
    
    def add(self, q: np.ndarray):
        ep, ep_level = insert(
            self._data,
            self._layers,
            q,
            self._ep,
            self._ep_level,
            self._n_established_connections,
            self._max_num_connections,
            self._n_candidates,
            self._norm_factor
        )
        self._ep = ep
        self._ep_level = ep_level


    def search(self, q: np.ndarray, k: int=5) -> list:
        pass
