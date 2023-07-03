#!/usr/bin/python3
"""This module has functions for the infamous N-queens problem"""
import sys


def checkPos(board, pos):
    """Function to check if a position is valid for a queen"""
    for r in range(pos[0]):
        if board[r][pos[1]] == 1:
            return False

    for r, p in zip(range(pos[0], -1, -1), range(pos[1], -1, -1)):
        if board[r][p] == 1:
            return False

    for r, p in zip(range(pos[0], -1, -1), range(pos[1], len(board), 1)):
        if board[r][p] == 1:
            return False

    return True


def nqueens(board, row, solutions):
    """Recursive function to try board layouts"""
    if row == len(board):
        solutions.append(conv(board))

    for r in range(len(board)):
        if checkPos(board, (row, r)) is True:
            board[row][r] = 1
            nqueens(board, row + 1, solutions)
            board[row][r] = 0


def conv(sol):
    """Function to convert styles of board descriptions"""
    fin = []
    for r in range(len(sol)):
        fin.append([])
        fin[r].append(r)
        for p in range(len(sol)):
            if sol[r][p] == 1:
                fin[r].append(p)
                break
    return fin


def main():
    """Main function to check args and call recursion"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * number for x in range(number)]
    sols = []
    nqueens(board, 0, sols)
    for x in sols:
        print(x)

if __name__ == "__main__":
    main()

