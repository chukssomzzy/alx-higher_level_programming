#!/usr/bin/env python3

def uppercase(str):
    strup = ""
    for str_c in str:
        if (ord(str_c) >= ord('a') and ord(str_c) <= ord('z')):
            strup = strup + chr((ord(str_c) - 32))
        else:
            strup = strup + str_c
    else:
        print("{}".format(strup));
