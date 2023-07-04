#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer or float.
        ValueError: If size is < 0.
        TypeError: If size is a float and less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
