#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner in the prime game

        Args:
            x (int): number of rounds
            num (arr):  an array of n

        Retrurn: winner or None if the winner cannot be determined
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        n = nums[round]

        if n == 1:
            Ben += 1
            continue

        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False

        prime_count = sum(primes)

        if prime_count % 2 == 1:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None

    return 'Maria' if Maria > Ben else 'Ben'
