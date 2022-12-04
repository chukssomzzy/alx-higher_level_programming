#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) <= 1:
        print("0 arguments.")
    elif len(argv) >= 2:
        argv_len = len(argv)
        if argv_len == 2:
            print("{} argument:".format(argv_len - 1))
        else:
            print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{}: {}".format(i, argv[i]))
