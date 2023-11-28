#!/usr/bin/python3
for decimal in range(0, 8):
    for units in range(decimal, 10):
        if decimal != units:
            print("{:d}{:d}".format(decimal, units), end=", ")
print("{:d}{:d}".format(decimal + 1, units))
