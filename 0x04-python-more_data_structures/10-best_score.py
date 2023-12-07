#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    my_list = list(a_dictionary.values())
    maximum = max(my_list)
    for name in a_dictionary:
        if a_dictionary[name] == maximum:
            return name
