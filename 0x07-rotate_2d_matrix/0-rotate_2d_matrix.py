#!/usr/bin/python3
"""Definition of function that rotates matrix"""


def rotate_2d_matrix(matrix):
    """function rotates 2d matrix"""
    matrix[:] = list(map(list, zip(*matrix)))
    for row in matrix:
        row[:] = row[::-1]
