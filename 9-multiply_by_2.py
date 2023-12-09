#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for valeur in a_dictionary:
        cle = a_dictionary[valeur] * 2
        new_dict.update({valeur: cle})
    return new_dict
