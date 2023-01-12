#!/usr/bin/python3

"""Load json from a file"""
import json


def load_from_json_file(filename):
    """Load json from a file

    Args:
        filename: filename of  file to deserialize json from

    """
    if type(filename) != str:
        return
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
