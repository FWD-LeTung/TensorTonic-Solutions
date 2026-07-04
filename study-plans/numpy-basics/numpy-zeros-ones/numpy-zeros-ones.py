import numpy as np

def create_filled_array(shape, kind):
    """
    Returns: 2D numpy array of given shape with dtype float64
    """
    x = tuple(shape)
    if kind == 'zeros':
        return np.zeros(x)
    return np.ones(x)
    pass