def check_sign(x: int):
    """Determines if 'x' is positive, negative, or zero"""
    if x < 0:
        return "negative"
    elif x > 0:
        return "positive"
    else:
        return "zero"


def is_prime(x: int):
    """Checks if a number is prime"""

    if x <= 1:
        return False

    # Check if divisble from 2 to x and return false if so
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def generate_primes():
    """Generates list of first 10 primes"""

    primes = []

    # Increment until 10 primes have been found
    num = 1
    while len(primes) != 10:
        # Add to list if prime found
        if is_prime(num):
            primes.append(num)

        num += 1

    return primes


def add_nums():
    """Calculates sum of all numbers from 1 to 100"""

    total = 0

    # Loop from 1 to 100 and add to total
    num = 1
    while num <= 100:
        total += num
        num += 1

    return total


if __name__ == "__main__":
    print("Sign of -3:", check_sign(-3))
    print("Is 17 prime?", is_prime(17))
    print("First 10 primes:", generate_primes())
    print("Sum of all numbers from 1 to 100:", add_nums())