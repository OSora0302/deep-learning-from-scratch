import numpy as np

def out(x, w, b):
    v = np.sum(x * w) + b
    return int(v > 0)

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -1
    return out(x, w, b)

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = 0
    return out(x, w, b)

def NAND(x1, x2):
    return 1 - AND(x1, x2)

def XOR(x1, x2):
    return AND(OR(x1, x2), NAND(x1, x2))

def check(G):
    for i in ([0, 0], [0, 1], [1, 0], [1, 1]):
        r = G(*i)
        print(str(i) + " -> " + str(r))

for i in (AND, OR, NAND, XOR):
    print()
    check(i)
