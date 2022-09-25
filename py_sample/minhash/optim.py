from scipy.integrate import quad


def calc_fp(threshold: float, b: int, r: int) -> tuple:
    p = lambda x: 1 - (1 - x**float(r)) ** float(b)
    y, _ = quad(p, 0.0, threshold)
    return y


def calc_fn(threshold: float, b: int, r: int) -> tuple:
    p = lambda x: 1 - (1 - (1 - x**float(r))**float(b))
    y, _ = quad(p, threshold, 1.0)
    return y


def optimal_param(threshold: float,
                  n_perm: int,
                  fp_weight: float=0.5,
                  fn_weight: float=0.5) -> tuple:
    min_error = float("inf")
    param = (0, 0)
    for i in range(1, n_perm+1):
        max_range = int(n_perm/i)
        for j in range(1, max_range+1):
            fp = calc_fp(threshold, i, j)
            fn = calc_fn(threshold, i, j)
            error = fp*fp_weight + fn*fn_weight
            if error < min_error:
                min_error = error
                param = (i, j)
    return param
