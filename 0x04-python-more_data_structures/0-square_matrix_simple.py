#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return the square of a matrix 2d elements
    """
    new_matrix = []
    for i in range(len(matrix)):
        tmp_matrix = []
        for j in range(len(matrix)):
            tmp_matrix.append(matrix[i][j]**2)
            if (j == len(matrix[i]) - 1):
                new_matrix.append(tmp_matrix)
    return (new_matrix)
