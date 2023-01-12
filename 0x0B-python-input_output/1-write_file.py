#!/usr/bin/python3

"""Write a string to a test file"""


def write_file(filename="", text=""):
    """Write a string to a file

    Args:
        filename (str): file to write to
        text (str): content to write to file

    Returns:
        Number of bytes written

    """
    if type(filename) != str or type(text) != str:
        return 0

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
