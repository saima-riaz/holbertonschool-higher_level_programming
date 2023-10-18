#!/usr/bin/python3
"""returns True if object is exactly an instance of the specified class
otherwise False"""


def is_same_class(obj, a_class):
    """class object"""
    return type(obj) is a_class
