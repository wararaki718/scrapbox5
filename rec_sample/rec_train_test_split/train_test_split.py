from typing import Tuple

import numpy as np
import scipy.sparse as sps


def train_test_split(x: sps.csr_matrix, test_ratio: float=0.2) -> Tuple[sps.csr_matrix, sps.csr_matrix]:
    x_ = x.tocoo()
    n_test = int(x.shape[1] * test_ratio)
    test_indices = np.unique(np.random.randint(0, x.shape[1], size=n_test))

    x_test = sps.csr_matrix(
        (
            x_.data[test_indices],
            (
                x_.row[test_indices],
                x_.col[test_indices]
            )
        ),
        shape=x.shape
    )
    x_train = sps.csr_matrix(
        (
            np.delete(x_.data, test_indices),
            (
                np.delete(x_.row, test_indices),
                np.delete(x_.col, test_indices)
            )
        ),
        shape=x.shape
    )

    return x_train, x_test
