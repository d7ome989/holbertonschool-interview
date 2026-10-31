#!/usr/bin/python3
"""Solve the N queens puzzle using backtracking."""
import sys


def is_safe(cols, row, col):
    """Check that a queen at (row, col) is not attacked by earlier rows."""
    for r in range(row):
        c = cols[r]
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve(n, row, cols):
    """Place queens row by row and print every full solution."""
    if row == n:
        print([[r, cols[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(cols, row, col):
            cols.append(col)
            solve(n, row + 1, cols)
            cols.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])
