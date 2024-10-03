#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner in the prime game

        Args:
            x (int): number of rounds
            num (arr):  an array of n

        Retrurn: winner or None if the winner cannot be determined
    """
    if not x or not nums:
        return None

    Ben = 0
    Maria = 0

    for round in range(x):
        n = nums[round]

        if n == 1:
            Ben += 1
            continue

        playing_numbers = list(range(2, n + 1))
        index = 0

        while (index < len(playing_numbers)):
            current_prime = playing_numbers[index]
            sieve_index = index + 1

            while (sieve_index < len(playing_numbers)):
                if playing_numbers[sieve_index] % current_prime == 0:
                    playing_numbers.pop(sieve_index)
                else:
                    sieve_index += 1

            index += 1

        prime_count = (len(playing_numbers))

        if prime_count % 2 == 1:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None

    return 'Ben' if Ben > Maria else 'Maria'
