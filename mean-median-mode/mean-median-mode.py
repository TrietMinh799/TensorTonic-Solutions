import numpy as np
from collections import Counter
from scipy import stats

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    a = np.asarray(x)
    return (np.mean(a), np.median(a), stats.mode(a, keepdims=False).mode)