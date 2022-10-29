import random
from typing import Tuple

import numpy as np
import scipy.sparse as sps


def train_test_split(x: sps.csr_matrix, test_ratio: float=0.2) -> Tuple[sps.csr_matrix, sps.csr_matrix]:
    test_data = []
    test_cols = []
    test_rows = []
    train_data = []
    train_cols = []
    train_rows = []
    for row in x:
        row_ = row.tocoo()

        if len(row_.data) == 0:
            train_data.extend(row_.data)
            train_cols.extend(row_.col)
            train_rows.extend(row_.row)
            continue

        n = max(int(len(row_.data) * test_ratio), 1)
        test_indices = random.sample(range(len(row_.data)), n)
        test_indices.sort()

        test_data.extend(row_.data[test_indices])
        test_cols.extend(row_.col[test_indices])
        test_rows.extend(row_.row[test_indices])

        train_data.extend(np.delete(row_.data, test_indices))
        train_cols.extend(np.delete(row_.col, test_indices))
        train_rows.extend(np.delete(row_.row, test_indices))

    import collections
    print(collections.Counter(test_data))
    print(len(test_data))
    print(len(test_cols))
    print(len(test_rows))
    x_test = sps.coo_matrix(
        (
            test_data,
            (
                test_rows,
                test_cols
            )
        ),
        shape=x.shape
    )

    print(collections.Counter(train_data))
    print(len(train_data))
    print(len(train_cols))
    print(len(train_rows))
    x_train = sps.coo_matrix(
        (
            train_data,
            (
                train_rows,
                train_cols
            )
        ),
        shape=x.shape
    )

    return x_train, x_test
