#!/usr/bin/python3

"""Remove by the c way"""


def remove_char_at(str, n):
    newstr = ""
    if str:
        for i in range(len(str)):
            if i != n:
                newstr += str[i]
        return newstr
