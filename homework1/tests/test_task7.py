from src import task7
import numpy as np
import pytest


# Make sure function multiplies valid matrices correctly
@pytest.mark.parametrize(
    "m1, m2, result",
    [
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[5, 6], [7, 8]]),
            np.array([[19, 22], [43, 50]]),
        ),
        (
            np.array([[2, 3], [4, 5]]),
            np.zeros((2, 2)),
            np.zeros((2, 2)),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6]]),
            np.array([[7, 8], [9, 10], [11, 12]]),
            np.array([[58, 64], [139, 154]]),
        ),
    ],
)
def test_multiply_matrices(m1, m2, result):
    calculated = task7.multiply_matrices(m1, m2)
    assert np.array_equal(calculated, result)

# Make sure function raises error when matrices are not compatible
@pytest.mark.parametrize(
    "m1, m2",
    [
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[5, 6], [7, 8], [9, 10]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6]]),
            np.array([[7, 8], [9, 10]]),
        ),
    ],
)
def test_invalid_matrices(m1, m2):
    with pytest.raises(ValueError):
        task7.multiply_matrices(m1, m2)

# Runt tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
