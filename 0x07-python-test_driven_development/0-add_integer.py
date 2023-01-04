#!/usr/bin/python3

"""add integer or float together
description:
    add_integer return the addition of two add_integer
    if the arg are not int and not float it raises
    exception (TypeError)

"""


def add_integer(a, b=98):
    """add two integer together
    Args:
        a (int): first integer
        b (int): second integer
    Raises:
        TypeError: if either A or B is not int
    Returns: summation of two ints
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
