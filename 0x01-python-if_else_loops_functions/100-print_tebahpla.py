#!/usr/bin/python3

"""prints ascii in reverse"""

if __name__ == "__main__":
    last_alpha = ord('z')
    for i in range(ord('z') - ord('a') + 1):
        if i % 2 != 0:
            last_alpha -= 32
        print(chr(last_alpha - i), end="")
        last_alpha = ord('z')
