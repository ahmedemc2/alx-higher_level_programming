#!/usr/bin/python3
import sys
lenght = len(sys.argv[1:])
sum = 0
for i in range(1, lenght + 1):
    sum = sum + int(sys.argv[i])
if __name__ == "__main__":
    print("{:d}".format(sum))
