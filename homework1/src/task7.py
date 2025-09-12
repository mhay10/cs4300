import numpy as np


def multiply_matrices(m1: np.ndarray, m2: np.ndarray):
    """Multiplies two matrices together"""

    # Format matrix shapes to check for correct dimensions
    m1_shape = (1,) + m1.shape if m1.ndim == 1 else m1.shape
    m2_shape = (1,) + m2.shape if m2.ndim == 1 else m2.shape
    print(m1_shape)
    print(m2_shape)

    # Check that multiplication is possible
    if m1_shape[1] != m2_shape[0]:
        raise ValueError("Matrix dimensions are not compatible")

    # # Multiply the matrices
    result = np.matmul(m1, m2)
    return result
