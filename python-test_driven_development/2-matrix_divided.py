#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number
    
    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (cannot be zero)
    
    Returns:
        New matrix with divided values rounded to 2 decimals
    
    Raises:
        TypeError: If matrix is invalid or div isn't a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num/div, 2) for num in row] for row in matrix]
