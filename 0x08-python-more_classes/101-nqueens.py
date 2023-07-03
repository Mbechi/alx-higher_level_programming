#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    # Base case: All queens have been placed
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)

def print_solutions(n, solutions):
    for sol in solutions:
        chessboard = []
        for i in range(n):
            chessboard.append([i, sol[i]])
        print(chessboard)

def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)
    print_solutions(n, solutions)

if __name__ == '__main__':
    main()
