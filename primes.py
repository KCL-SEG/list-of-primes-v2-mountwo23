"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError('error')
    list = []
    currentNumber = 2
    for x in range(number_of_primes):
        y = x + 1
        while len(list) < y:
            if is_prime(currentNumber):
                list.append(currentNumber)
            currentNumber = currentNumber + 1
    return list


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True
