# Author: Matthew Armstrong
# Date: 10/28/2021
# Description: Write a recursive function named row_puzzle
# that takes a list of integers as a parameter and returns True if the puzzle is solvable for that row,
# but returns False otherwise.

def row_puzzle(squares):
    """function which checks if a square was visited"""
    visited = []
    for i in range(len(squares)):
        visited.append(0)
    return helper_puzzle(squares, 0, visited)


def helper_puzzle(squares, pos, visited):
    """recursive function that takes a list of integers as a parameter and returns True if the puzzle is solvable for that row,
    but returns False otherwise"""
    if pos == len(squares) - 1:
        return True
    elif pos > len(squares) - 1 or pos < 0:
        return False
    elif visited[pos] != 0:
        return False
    left = False
    right = False
    visited[pos] = 1
    if pos - squares[pos] >= 0:
        left = helper_puzzle(squares, pos - squares[pos], visited)
    if pos + squares[pos] < len(squares):
        right = helper_puzzle(squares, pos + squares[pos], visited)
    return left or right


# print(row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0]))
# print(row_puzzle([1, 3, 2, 1, 3, 4, 0]))
