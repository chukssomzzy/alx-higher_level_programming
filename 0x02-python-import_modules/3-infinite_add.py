#!/usr/bin/python3

from sys import argv, exit
if __name__ != "__main__":
    exit()
arg_len = len(argv)
sum = 0
for i in range(1, arg_len):
    sum += int(argv[i])
print("{}".format(sum))

