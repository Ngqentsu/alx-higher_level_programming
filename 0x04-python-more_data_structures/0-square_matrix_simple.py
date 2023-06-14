#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row.copy() for row in matrix]

    for i in range(len(matrix)):
        new_matrix[i] = [element**2 if isinstance(element, int) else element for element in matrix[i]]
    return new_matrix