#!/usr/bin/python3
"""Definition of function isWinner"""


def is_prime(num):
    """determine if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """gets all prime numbers"""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    """determines who winner of each game is"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        num_primes = len(primes)

        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
        if maria_wins > ben_wins:
            return "Maria"
        elif ben_wins > maria_wins:
            return "Ben"
        else:
            return None
