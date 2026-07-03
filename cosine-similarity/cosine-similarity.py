import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    np.asarray(a)
    np.asarray(b)
    x = np.linalg.norm(a)
    y = np.linalg.norm(b)
    if x == 0 or y == 0:
        return 0.0
    return np.dot(a,b)/(x*y)
    