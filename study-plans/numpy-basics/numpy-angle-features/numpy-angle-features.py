import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    x = np.asarray(angles, dtype=np.float64)
    y = np.array([np.sin(x), np.cos(x), np.tan(x)])

    return y
    