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
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    size = 0
    if isinstance(matrix, list):
        inner_mat = []
        for ilist in matrix:
            if isinstance(ilist, list):
                if not size:
                    size = len(ilist)
                if size != len(ilist):
                    raise TypeError("Each row of the matrix must have the same size")
                for num_int in ilist:
                    if type(num_int) == int or type(num_int) == float:
                        inner_mat.append(round(num_int / div, 2))
                    else:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    new_matrix.append(inner_mat)
                    inner_mat = []
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        return new_matrix
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
