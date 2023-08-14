#!/usr/bin/python3
"""
Program solves the N Queens Problem
using backtracking algorithm
"""
import sys


def check_valid(board, row, col):
    "Check for validility on the board"
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1

    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    "Solve the N Queens Problem"
    if row == len(board):
        sol = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    sol.append([i, j])
        print(sol)
        return

    for col in range(len(board)):
        if check_valid(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(N)] for _ in range(N)]

    solve_nqueens(board, 0)
