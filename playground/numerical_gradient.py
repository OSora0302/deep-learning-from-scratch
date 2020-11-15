import numpy as np

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fx_h1 = f(x)

        x[idx] = tmp_val - h
        fx_h2 = f(x)

        grad[idx] = (fx_h1 - fx_h2) / (2*h)
        x[idx] = tmp_val
    
    return grad

