#!/usr/bin/python3
"""Declare a class Square."""


class Square:
    """Represent a square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with size 0.

        Args:
            size (int): The size of the square
            position (int, int): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The value size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
