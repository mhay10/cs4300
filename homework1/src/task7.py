import numpy as np


# def multiply_matrices(m1: np.ndarray, m2: np.ndarray):
#     """Multiplies two matrices together"""

#     # Format matrix shapes to check for correct dimensions
#     m1_shape = (1,) + m1.shape if m1.ndim == 1 else m1.shape
#     m2_shape = (1,) + m2.shape if m2.ndim == 1 else m2.shape

#     # Check that multiplication is possible
#     if m1_shape[1] != m2_shape[0]:
#         raise ValueError("Matrix dimensions are not compatible")

#     # # Multiply the matrices
#     result = np.matmul(m1, m2)
#     return result

def multiply_matrices(m1: np.ndarray, m2: np.ndarray):
    """Multiplies two matrices together"""

    # Check that the matrices are 0D, 1D, or 2D
    if m1.ndim > 2 or m2.ndim > 2:
        raise ValueError("Only 0D, 1D, and 2D matrices are supported")

    # Turn 0D into (1,1) and 1D into (1,n) matrices
    if m1.ndim == 0:
        m1 = m1.reshape((1, 1))
    elif m1.ndim == 1:
        m1 = m1.reshape((1, m1.shape[0]))

    if m2.ndim == 0:
        m2 = m2.reshape((1, 1))
    elif m2.ndim == 1:
        m2 = m2.reshape((1, m2.shape[0]))
    
    # Chcek that the matrices are compatible
    if m1.shape[1] != m2.shape[0]:
        raise ValueError(f"Matrix multiplication between {m1.shape} and {m2.shape} is not possible")

    # Multiply the matrices
    result = np.matmul(m1, m2)
    return result