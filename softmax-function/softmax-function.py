import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    arr = np.asarray(x, dtype=np.float64)

    if arr.ndim == 1:
        e = np.exp(arr - np.max(arr))
        sum = np.sum(e) 
        return e/sum
    e = np.exp(arr - np.max(arr, axis=1, keepdims=True))
    
    return e / np.sum(e, axis=1, keepdims=True)