#!/usr/bin/python3
"""making change module"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """make change doc"""
    if total <= 0:
        return -1
    t = total
    num_of_coins = 0

    coins = sorted(coins, reverse=True)
    for i in range(len(coins)):
        if total == 0:
            break
        if (i == len(coins) - 1 and total % coins[i] > 0):
            return -1
        num_of_coins += total // coins[i]
        total = total % coins[i]
    return num_of_coins
