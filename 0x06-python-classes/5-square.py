#!/usr/bin/python3
"""class that define a square"""


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int): lenght of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the lenght of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Area of this square.

        Returns:
            int: The size squared.
        """
        return self.__size**2

    def my_print(self):
        """ draw the table using hashtags """
        lenght = self.__size
        if lenght != 0:
            for i in range(lenght):
                for j in range(lenght):
                    print("#", end="")
                print()
        else:
            print()
