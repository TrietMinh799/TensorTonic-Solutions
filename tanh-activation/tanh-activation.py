import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    _x = np.asarray(x);
    # Write code here
    return (np.exp(_x) - np.exp(-_x)) / (np.exp(_x) + np.exp(-_x))