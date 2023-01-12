#!/usr/bin/python3

"""Append a str to end of file"""


def append_write(filename="", text=""):
    """Append a str to the end of file

    Args:
        filename (str): filename to append text to
        text (str): str to append to filename
    Returns:
        The numbers of byte written
    """
    if type(filename) != str or type(text) != str:
        return
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
