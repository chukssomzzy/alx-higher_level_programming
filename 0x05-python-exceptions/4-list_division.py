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
    for i in range(list_length):
        try:
            newList.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            newList.insert(i, 0)
            print("wrong type")
        except ZeroDivisionError:
            newList.insert(i, 0)
            print("division by 0")
        except IndexError:
            newList.insert(i, 0)
            print("out of range")
    return newList
