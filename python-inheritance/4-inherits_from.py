#!/usr/bin/python3
"""function that return True obj is instance class
that inherited"""


def inherits_from(obj, a_class):
    """obj of the class"""
    return type(obj) != a_class
