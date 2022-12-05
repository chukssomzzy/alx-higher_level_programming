#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit(1)
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
opdic = {"+": add, "-": sub, "/": div, "*": mul}
for op in opdic:
    if op == argv[2]:
        break;
else:
    print("Uknown operator. Available operators: +, -, * and /")
    exit(1)
func = opdic[argv[2]]
if (func):
    print("{} {} {} = {}".format(a, argv[2], b, func(a, b)))
