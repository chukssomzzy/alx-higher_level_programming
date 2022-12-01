#!/usr/bin/env python3

def print_last_digit(num):
    num = abs(num) % 10
    print("{}".format(num), end="")
    return (num)
