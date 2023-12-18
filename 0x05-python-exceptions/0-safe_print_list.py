#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nbrPrint = 0
        for element in my_list:
            print("{}".format(element), end="")
            nbrPrint += 1
            if nbrPrint == x:
                break
        print()
    except IndexError:
        print("out of range")
    return nbrPrint
