#!/usr/bin/python3
""" finds a peak in a list """


def find_peak(list_of_integers):

    for i in range(len(list_of_integers)):
        if i - 1 >= 0:
            if list_of_integers[i] >= \
                    list_of_integers[i - 1] and list_of_integers[i] >= \
                    list_of_integers[i + 1]:
                return list_of_integers[i]
        elif list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
        elif len(list_of_integers) == 0 or i == (len(list_of_integers) - 1) \
                and list_of_integers[i] > list_of_integers[i - 1]:
            return list_of_integers[i]
