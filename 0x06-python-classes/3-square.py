#!/usr/bin/python3
""" class that define a square """


class Square:
    """ definig the square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ calculate the area of the square """
    def area(self):
        return self.__size**2
