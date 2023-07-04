#!/usr/bin/python3
"""Declare a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): list of lists of integers or floats
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the elements divided by the given number.

    Raises:
        TypeError: If the matrix is not a valid matrix (list of lists of integers/floats),
            or if each row of the matrix does not have the same size.
        TypeError: If the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])