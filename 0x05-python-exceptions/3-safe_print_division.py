#!/usr/bin/python3

def safe_print_division(a, b):
    """Prints the result of division of two integers

    Args:
        a (int): integer a
        b (int): integer b

    Returns:
        return (a / b)
    """
    res = None
    try:
      res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
