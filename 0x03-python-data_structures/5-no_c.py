#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for i in range(0, len(my_list)):
        if my_list[i] == "c" or my_list[i] == "C":
            for j in range(i, len(my_list) - 1):
                my_list[j] = my_list[j + 1]
            my_list[-1] = ""
            i -= 1
    new_string = "".join(my_list)
    return new_string
