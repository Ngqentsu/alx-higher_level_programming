#!/usr/bin/python3
"""Declare a class Square."""


class Square:
    """Represent a square object."""

    def __init__(self, size=0):
        """Initializes a Square instance with size 0.

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

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

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check for equality comparison in areas of two squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check for non equality comparison in areas of two squares."""
        return self.area() != other.area()

    def __ge__(self, other):
        """Check if the area of the first square is >= to the second square."""
        return self.area() >= other.area()

    def __le__(self, other):
        """Check if the area of the first square is =< to the second square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of the first square is > the second square."""
        return self.area() > other.area()

    def __lt__(self, other):
        """Check if the area of the first square is < the second square."""
        return self.area() < other.area()
