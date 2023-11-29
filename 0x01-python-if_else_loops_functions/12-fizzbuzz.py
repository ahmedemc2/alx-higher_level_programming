#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        value = " " if i < 100 else ""
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=value)
        elif i % 3 == 0:
            print('Fizz', end=value)
        elif i % 5 == 0:
            print('Buzz', end=value)
        else:
            print('{:d}'.format(i), end=value)
