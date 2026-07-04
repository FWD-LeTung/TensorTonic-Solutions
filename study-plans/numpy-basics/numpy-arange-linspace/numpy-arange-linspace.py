import numpy as np

def create_sequence(start, stop, param, kind):
    
    if kind == 'linspace':
        a = np.empty(param)
        step = (stop-start)/(param-1)
        
        for i in range(param):
            a[i] = start + i*step
        return a
    else:
        a = []
        x = start
        while x < stop:
            a.append(x)
            x+=param
        return np.asarray(a, dtype=np.float64)