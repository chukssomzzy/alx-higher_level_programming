#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return the square of a matrix 2d elements
    """
    ret_red = lambda m: [x ** 2 for x in m]
    new_matrix = [ret_red(row) for row in matrix]
    return (new_matrix)
