#!/usr/bin/python3
for tens in range(0, 8):
    for units in range(tens, 10):
        if tens == units:
            continue
        print("{:d}{:d}".format(tens, units), end=", ")
tens += 1
print("{:d}{:d}".format(tens, units))
