#!/usr/bin/python3
"""Definition of function isWinner"""


def get_primes(n):
    """gets all prime numbers"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    """determines who winner of each game is"""
    if x < 0:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = get_primes(max_n)

    for n in nums:
        if n == 0:
            continue

        if n in primes:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
