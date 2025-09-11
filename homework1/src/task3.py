def check_sign(x: int):
    if x < 0:
        return "negative"
    elif x > 0:
        return "positive"
    else:
        return "zero"


def is_prime(x: int):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def generate_primes():
    primes = []
    num = 1
    while len(primes) != 10:
        if is_prime(num):
            primes.append(num)

        num += 1

    return primes


def add_nums():
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1

    return total
