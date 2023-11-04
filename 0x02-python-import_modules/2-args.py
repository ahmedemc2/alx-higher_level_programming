#!/usr/bin/python3

import sys

lenght = len(sys.argv)
index = 1
if __name__ == "__main__":
    if lenght == 1:
        print("{:d} arguments.".format(lenght - 1))
    else:
        print("{:d} arguments:".format(lenght - 1))
    while index < lenght:
        print("{:d}: {}".format(index, sys.argv[index]))
        index += 1
