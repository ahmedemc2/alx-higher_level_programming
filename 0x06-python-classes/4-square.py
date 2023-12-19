#!/usr/bin/python3
""" class that define a square """


class Square:
    def __init__(self, size=0):
        """ Constructor.

        Args:
            size: lenght of a side of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Property for the lenght of a side of this square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) != int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size**2
