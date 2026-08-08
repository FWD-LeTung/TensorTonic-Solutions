import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    data = x.copy()
    y = np.asarray(x)
    x_mean = np.mean(y)
    x_median = np.median(y)
    
    counter = Counter(data)
    mode_tuple = counter.most_common(1)[0]
    mode_value = mode_tuple[0]
    
    return (x_mean, x_median, mode_value)