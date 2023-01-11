#!/usr/bin/python3

"""Read a file and print to stdout"""

def read_file(filename=""):
    """Read content of filename and print output to stdout

    Args:
        filename (str): location of file
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print()
