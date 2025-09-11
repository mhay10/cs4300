from src import task3
import pytest

# Make sure signs are correct
@pytest.mark.parametrize(
    "num, sign",
    [
        (-5, "negative"),
        (0, "zero"),
        (5, "positive"),
    ],
)
def test_num_signs(num, sign):
    assert task3.check_sign(num) == sign

# Make sure prime numbers are correctly identified
@pytest.mark.parametrize(
    "num, result",
    [
        (1, False),
        (2, True),
        (4, False),
        (41, True),
        (100, False),
    ],
)
def test_prime_check(num, result):
    assert task3.is_prime(num) == result

# Make sure first 10 primes match
def test_primes():
    primes = task3.generate_primes()
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Test sure sum of first 100 numbers is same
def test_sum_range():
    assert task3.add_nums() == 5050

# Run tests
if __name__ == "__main__":
    test_num_signs()
    test_prime_check()
    test_primes()
    test_sum_range()
