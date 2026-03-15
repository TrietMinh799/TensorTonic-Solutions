import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    t = np.asarray(k);
    return ((np.multiply(p, (1 - p)**np.subtract(k, 1))), 1 / p)