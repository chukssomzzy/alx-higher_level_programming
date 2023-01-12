#!/usr/bin/python3

"""save and convert object to json"""
import json


def save_to_json_file(my_obj, filename):
    """Save convert object to file

    Args:
        filename (str): filename of file to save to
        my_obj (obj): object to serialize
    """
    if type(filename) != str:
        return
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
