#!/usr/bin/python3
"""class that define a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size (int): lenght of a side of the square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the lenght of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/Set the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            (not isinstance(value, tuple))
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
        ) or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of this square.

        Returns:
            int: The size squared.
        """
        return self.__size**2

    def my_print(self):
        """draw the table using hashtags"""
        lenght = self.__size
        if lenght == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, lenght):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, lenght)]
            print("")
