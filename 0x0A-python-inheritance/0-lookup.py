#!/usr/bin/python3
"""
Module: lookup

Description: Function that returns list of attributes and methods of an object.

Functions:
    lookup(obj) -> list
"""


def lookup(obj):
    """Returns a list of available attributes of an object."""
    return (dir(obj))
