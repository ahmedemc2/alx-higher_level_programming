#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in rows:
            value = " " if column != rows[-1] else ""
            print("{:d}".format(column), end=value)
        print()
