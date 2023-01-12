#!/usr/bin/python3

"""Returns a json representation of an obj"""
import json


def to_json_string(my_obj):
    """Returns json representation of an object

    Args:
        my_obj: obj to stringify
    """
    return (json.dumps(my_obj))
