import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    arr = np.asarray(x, dtype=np.float64)
    result = np.where(arr < 0, alpha*arr, arr)
    return result