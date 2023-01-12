#!/usr/bin/python3

"""return json representation of an object __dict__"""


def class_to_json(obj):
    """Return dict of a class_to_json

    Args:
        obj: object
    """
    return obj.__dict__
