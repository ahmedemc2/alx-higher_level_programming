#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iterator = 0
    errors = 0
    while iterator < x:
        try:
            print("{:d}".format(my_list[iterator]), end="")
        except (TypeError, ValueError):
            None
            errors += 1
        iterator += 1
    print()
    return iterator - errors
