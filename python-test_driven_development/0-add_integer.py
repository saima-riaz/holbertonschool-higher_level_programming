#!/usr/bin/python3
"""define function add two integers"""


def add_integer(a, b=98):
    """function that add two intergers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        """If 'b' is a float, cast it to an integer"""
    return int(a) + int(b)
