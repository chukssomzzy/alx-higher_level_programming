#!/usr/bin/python3

"""add a method to json"""


class Student:
    """Defines  a student class"""

    def __init__(self, first_name, last_name, age):
        """Intialize a student

        Args:
            first_name:  defines student first first_name
            last_name: defines student last last_name
            age: defines age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrievea dict rep"""
        if not attrs or type(attrs) != list:
            return self.__dict__
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}
