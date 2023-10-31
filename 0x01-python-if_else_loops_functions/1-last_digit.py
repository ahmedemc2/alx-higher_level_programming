#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    str = f"Last digit of {number} is {last_digit} and is greater that 5"
elif last_digit == 0:
    str = f"Last digit of {number} is {last_digit} and is 0"
else:
    str = f"Last digit of {number} is {last_digit} and is less than 6\
 and not 0"
print(str)
