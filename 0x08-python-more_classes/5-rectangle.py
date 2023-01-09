#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """init a new rectangle

        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get and set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get and set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if not self.__width or not self.__height:
            return (0)
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """stringify triangle"""
        str = ""
        if not self.__width or not self.__height:
            return ""
        for i in range(self.height):
            str += "#" * self.__width
            if (i + 1) < self.height:
                str += '\n'
        return str

    def __repr__(self):
        """returns  a string representation of the class that can be parsed by
        eval"""
        return ("Rectangle(" + str(self.__width) + ", " + str(self.__height) +
                ")")

    def __del__(self):
        """call on delete of an instance"""
        print("Bye rectangle...")
