#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """call a function pointer with args

    Args:
        fct: function pointer
        args: pointer to all argument passed to fct
    Returns:
        the return value of fct
    """
    try:
        fct_ret = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
    return fct_ret
