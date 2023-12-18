#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbrPrint = 0
    try:
        while nbrPrint is not x:
            print("{}".format(my_list[nbrPrint]), end="")
            nbrPrint += 1
    except IndexError:
        None
    print()
    return nbrPrint
