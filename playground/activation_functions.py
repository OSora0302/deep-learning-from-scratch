import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

def check(f):
    x = np.arange(-5.0, 5.0, 0.1)
    y = f(x)
    plt.plot(x, y)
    plt.show()
