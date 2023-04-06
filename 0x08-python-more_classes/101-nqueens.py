#!/usr/bin/python3
"""
nqueens_backtracking.py: Finds all solutions
to the n-queens problem using backtracking.
"""
from sys import argv

if __name__ == "__main__":
    a = []
    # Ensure correct usage and input value
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize answer list
    for i in range(n):
        a.append([i, None])

    def queen_in_column(y):
        """Checks if a queen already exists in the specified column."""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def is_solution(x, y):
        """Checks if a given position is a valid solution."""
        if queen_in_column(y):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_answers_from(x):
        """Clears the answers from the point of failure onwards."""
        for i in range(x, n):
            a[i][1] = None

    def n_queens_recursive(x):
        """Recursive function to find all solutions."""
        for y in range(n):
            clear_answers_from(x)
            if is_solution(x, y):
                a[x][1] = y
                if x == n - 1:
                    print(a)  # Accepts solution
                else:
                    n_queens_recursive(x + 1)  # Moves on to next x value

    # Start recursive process at x = 0
    n_queens_recursive(0)
