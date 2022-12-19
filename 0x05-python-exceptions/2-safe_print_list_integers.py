#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints integers in a my_list
    Args;
        my_list (list): lists Args
        x (int): number of elements to print from the list

    Returns:
        The number of elements printed from the list
        """
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return printed
