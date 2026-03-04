import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    values = np.asarray(x);
    weight = np.asarray(p);

    if weight.sum() != 1:
        raise ValueError("The probability is invalid")

    return (values * weight).sum() / weight.sum();
