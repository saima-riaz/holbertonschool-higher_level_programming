#!/usr/bin/python3
"""A class representing a square.
    Private attribute:__size(int)
"""


class Square:
    def area(self):
            """initalizes square area"""
            return self.__size ** 2

    def __int__(self, size=0):
        """initalizes a new square"""

        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
