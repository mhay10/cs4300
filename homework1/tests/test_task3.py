from src import task3


def test_num_signs():
    assert task3.check_num(-5) == "negative"
    assert task3.check_num(0) == "zero"
    assert task3.check_num(5) == "positive"


def test_primes():
    primes = task3.generate_primes()
    for prime in primes:
        assert task3.is_prime(prime)


def test_sum_range():
    assert task3.add_nums() == 5050


if __name__ == "__main__":
    test_num_signs()
    test_primes()
    test_sum_range
