#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a 2D matrix."""
    return [[num ** 2 for num in row] for row in matrix]
