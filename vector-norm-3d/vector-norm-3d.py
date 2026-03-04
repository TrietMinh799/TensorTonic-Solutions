import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    points = np.square(np.asarray(v))
    axis = 1
    if points.ndim == 1:
        axis = 0
    return np.sqrt(np.sum(points, axis=axis))