#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Print int while print err to stderr

    Args:
        value (int): int to print

    Returns:
        true or False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    return True
