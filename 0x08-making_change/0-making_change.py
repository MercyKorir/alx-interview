#!/usr/bin/python3
"""Definition of function makeChange"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """determines fewest coins needed to meet a total"""
    count = 0
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    for item in coins:
        while item <= total:
            total -= item
            count += 1
    if total > 0:
        return -1
    else:
        return count
