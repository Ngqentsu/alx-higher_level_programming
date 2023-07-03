#!/usr/bin/python3
"""Declare a class Rectangle."""


class Rectangle:
    """Represent a rectangle object."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with width and height of 0.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The value width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """prints in stdout the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []

        for _ in range(self.__height):
            rectangle.append('#' * self.__width)
            if _ != self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
