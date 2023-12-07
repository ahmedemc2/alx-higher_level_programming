#!/usr/bin/python3
def best_score(a_dictionary):
    my_list = list(a_dictionary.values())
    maximum = max(my_list)
    for name in a_dictionary:
        if a_dictionary[name] == maximum:
            print(name)
