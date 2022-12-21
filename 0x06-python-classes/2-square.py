#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Describes the square class"""

    def __init__(self, size=0):
        """Initialize a new square obj

        Args:
            size (int): The size of new square gt 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
