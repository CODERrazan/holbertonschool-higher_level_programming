#!/usr/bin/python3
import sys

def infinite_add():
    sum = 0
    for arg in sys.argv[1:]:
        sum += int(arg)
    print(sum)

if __name__ == "__main__":
    infinite_add()
