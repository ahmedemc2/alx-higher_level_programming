#!/usr/bin/python3
""" square module that define a private instance """


class Square:
    """ Defines a square using a private instance attribute : size """
    def __init__(self, height):
        self.__size = height
