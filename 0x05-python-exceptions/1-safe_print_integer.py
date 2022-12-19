#!/usr/bin/python3

def safe_print_integer(value):
    """Prints a integer value

    Args:
        value (int): integer value to Prints

    Returns:
        onsuccess true
        """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
