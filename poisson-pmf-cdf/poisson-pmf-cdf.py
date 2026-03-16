import numpy as np
from scipy.special import factorial

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    return (((np.exp(-lam) * np.pow(lam, k)) / factorial(k)), np.sum([(np.exp(-lam)*np.pow(lam, x)) / (factorial(x)) for x in range(0, k + 1)]))