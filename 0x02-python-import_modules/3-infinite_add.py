#!/usr/bin/python3

import sys
lenght = len(sys.argv)
somme = 0

if __name__ == "__main__":
    for index in range(1, lenght):
        somme += int(sys.argv[index])
    print("{:d}".format(somme))
