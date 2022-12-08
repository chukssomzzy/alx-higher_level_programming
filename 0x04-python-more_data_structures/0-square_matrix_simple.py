#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return the square of a matrix 2d elements
    """
    new_matrix = [reduce_mat(row) for row in matrix]
    return (new_matrix)


def reduce_mat(matrix=[]):
    return ([x ** 2 for x in matrix])
