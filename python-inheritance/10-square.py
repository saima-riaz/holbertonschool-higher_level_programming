#!/usr/bin/python3

"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """base geometry"""
    def area(self):
        """ area define"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define class square(Rectangle)"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ define area"""
        return self.__size ** 2
