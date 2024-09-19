#!/usr/bin/python3
"""
Make change task
"""


def makeChange(coins, total):

    """ determine the fewest number of coins needed to
        meet a given amount total
        Args:
            - coins: list of the values of the coins
            in your possession
            - total: amount of change required
        Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_needed = 0
    for coin in coins:
        if total / coin > 0:
            coins_needed = coins_needed + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or coins_needed == 0:
        return -1
    return coins_needed
