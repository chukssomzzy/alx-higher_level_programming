#!/usr/bin/python3

"""Return list of list of integers containing pascal triangle"""


def pascal_triangle(n):
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        inner_tri = []
        for j in range(len(triangle[i]) + 1):
            if not j or j == len(triangle[i]):
                inner_tri.append(1)
            else:
                inner_tri.append(triangle[i][j] + triangle[i][j - 1])
        else:
            triangle.append(inner_tri)
    else:
        return triangle
