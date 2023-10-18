#!/usr/bin/python3
""" class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define int validator"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
