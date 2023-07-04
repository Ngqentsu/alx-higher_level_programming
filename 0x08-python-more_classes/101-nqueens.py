#!/usr/bin/python3
"""Solves N-queens puzzle, placing N non-attacking queens on N×N chessboard"""


import sys


def init_board(N):
    """Initialize an 'N' x 'N' chessboard."""
    board = []
    [board.append([]) for _ in range(N)]
    [row.append(' ') for _ in range(N) for row in board]
    return board


def is_valid(board, row, col, n):
    """Check if placing a queen at the given position is valid."""
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row, N, solutions):
    """Utility function to solve the N queens problem recursively."""
    if row == N:
        solution = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 'Q':
                    solution.append([r, c])
        solutions.append(solution)
        return

    for col in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = 'Q'
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = ' '


def solve_nqueens(N):
    """Solve the N queens problem."""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = init_board(N)
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    """Main function of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
