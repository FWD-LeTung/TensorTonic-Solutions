import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    x = np.asarray(data, dtype=np.float64)
    if operation == 'flatten':
        return x.flatten()
    elif operation == 'transpose':
        return x.T
    else:
        return np.expand_dims(x, axis=0)