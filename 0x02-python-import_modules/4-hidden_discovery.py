#!/usr/bin/python3
import sys
import hidden_4
if __name__ != "__main__":
    sys.exit(1)
def_names = dir(hidden_4)
for name in def_names:
    if name[:2] != "__":
        print(name)

