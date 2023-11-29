#!/usr/bin/python3
def remove_char_at(str, n):
    m = 0
    if (len(str) > n and n >= 0):
        if n == 0:
            m = 1
        str = str[m:n] + str[n + 1:]
    return str
