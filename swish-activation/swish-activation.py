import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=np.float32)
    sigmoid = 1 / (1 + np.exp(-x))
    return x * sigmoid