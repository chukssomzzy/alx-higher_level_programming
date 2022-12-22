#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element in list 1 by element in list 2

    Args:
        my_list_1 (list): contains the first my_list_1
        my_list_2 (list): contains the second list
        list_length (int): contains the size of the return list
    Returns:
        a list of  len list_length
    """
    newList = []
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newList.insert(i, div)
            div = 0
    return newList
