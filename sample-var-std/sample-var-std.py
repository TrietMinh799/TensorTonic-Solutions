import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    avg = np.mean(x)
    n = len(x)
    s = (1 / (n - 1)) * np.sum([(element - avg)**2 for element in x]);
    return s, np.sqrt(s);