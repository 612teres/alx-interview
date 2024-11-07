#!/usr/bin/python3
"""
N Queens Problem: Solves the N Queens problem using backtracking.
"""

import sys


def print_usage():
    print("Usage: nqueens N")
    exit(1)


# Argument validation
if len(sys.argv) != 2:
    print_usage()

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)


def solve_nqueens(n):
    """Solve the N-Queens problem using backtracking."""
    solutions = []
    board = [-1] * n  # Each index represents a row, value represents column

    def is_safe(row, col):
        """Check if placing a queen at (row, col) is safe."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def place_queen(row):
        """Recursive function to place queens and find solutions."""
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row + 1)
                board[row] = -1

    place_queen(0)
    return solutions


for solution in solve_nqueens(n):
    print(solution)
