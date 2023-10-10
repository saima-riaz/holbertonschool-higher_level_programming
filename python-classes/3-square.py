#!/usr/bin/python3
class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializes a new Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """define square area"""
        return self.__size ** 2
