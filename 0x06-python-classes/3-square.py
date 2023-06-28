#!/usr/bin/python3
"""Declare a class Square."""


class Square:
    """Represent a square object."""

    def __init__(self, size=0):
        """Initializes a Square instance with size 0.

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
