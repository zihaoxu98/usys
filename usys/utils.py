import numpy as np

def differ_by_null(x1, x2, null_space):
    dim_diff = [x1 - x2]
    dim_diff.extend(null_space)
    return np.linalg.matrix_rank(null_space) == np.linalg.matrix_rank(dim_diff)

def hot_array(length, zero_indices):
    if np.any(np.array(zero_indices) < 0) or np.any(np.array(zero_indices) >= length):
        raise ValueError("Invalid value of zero_indices")
    result = np.zeros(length)
    if isinstance(zero_indices, int):
        result[zero_indices] = 1
    elif len(zero_indices) > 0:
        result[zero_indices] = 1
    else:
        pass
    return result
