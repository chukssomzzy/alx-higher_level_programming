#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = abs(number) % 10
if (number < 0):
    lastnum = -lastnum
str = f"last digit of {number} is {lastnum} "
if lastnum > 5:
    print(str + "and is greater than 5")
elif lastnum == 0:
    print(str + "and is 0")
elif lastnum < 6 and not 0:
    print(str + "and is less than 6 and not 0")
