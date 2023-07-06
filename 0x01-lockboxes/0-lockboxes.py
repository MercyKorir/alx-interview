#!/usr/bin/python3
"""Defines a function canUnlockAll"""


def canUnlockAll(boxes):
    """
    The user inputs a list of lists
    Returns True if all boxes can be opened
    Otherwise returns False
    """

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    temp = [0]
    while temp:
        box = temp.pop()
        for key in boxes[box]:
            if key >= 0 and key < n and not opened[key]:
                opened[key] = True
                temp.append(key)

    return all(opened)
