#!/usr/bin/python3

"""return a python object from string"""
import json


def from_json_string(my_str):
    """Convert json to python obj

    Args:
        my_str: json to convert to python object
    """
    return json.loads(my_str)
