#!/usr/bin/python3

"""return json representation of an object __dict__"""
import json


def class_to_json(obj):
    """Return dict of a class_to_json

    Args:
        obj: object
    """
    return json.dumps(obj.__dict__)
