#!/usr/bin/python3
"""Definition of function isWinner"""


def isWinner(x, nums):
    """determines who winner of each game is"""
    def calculate_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        curr_prime = 2
        while curr_prime * curr_prime <= n:
            if primes[curr_prime]:
                for i in range(curr_prime * curr_prime, n + 1, curr_prime):
                    primes[i] = False
            curr_prime += 1
        return [i for i in range(2, n + 1) if primes[i]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = calculate_primes(n)
        remaining_numbers = list(range(1, n + 1))
        maria_turn = True

        while primes and remaining_numbers:
            chosen_prime = min(primes)
            primes.remove(chosen_prime)
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                if multiple in remaining_numbers:
                    remaining_numbers.remove(multiple)

            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
