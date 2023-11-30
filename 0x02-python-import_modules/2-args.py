#!/usr/bin/python3
import sys
listOfArgs = sys.argv[1:]
lenght = len(listOfArgs)
if __name__ == "__main__":
    value = "s.\n" if lenght == 0 else ":\n" if lenght == 1 else "s:\n"
    print("{:d} argument".format(lenght), end=value)
    for i in range(1, lenght + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
