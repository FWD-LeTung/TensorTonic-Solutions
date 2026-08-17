import numpy as np

def matrix_inverse(A):
    A = np.asarray(A, dtype=float)

    if A.shape[0] != A.shape[1]:
        return None

    if np.linalg.matrix_rank(A) < A.shape[0]:
        return None

    return np.linalg.inv(A)