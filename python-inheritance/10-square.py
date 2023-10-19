#!/usr/bin/python3
"""mention Rectangle"""

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
