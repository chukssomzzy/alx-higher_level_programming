#!/usr/bin/python3
"""Divide each element in a square matrix by a scalar Div """


def matrix_divided(matrix, div):
    """Divide each element of a matrix by a scalar

    Args:
        matrix (list of list): contains list of list of integers
        div (int): non zero divisor
    Returns:
        new_matrix: list of list containing that has been divided by div
    Raises:
        TypeError: when not a matrix or when div is zero or element of matrix
        is not a number
        ZeroDivisionError: division by zero
        TypeError: div must be a number
        TypeError: Each row of the matrix have the same size
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, float) or isinstance(elem, int) for row in
                    matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
