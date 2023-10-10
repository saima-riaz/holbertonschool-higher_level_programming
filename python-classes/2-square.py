#!/usr/bin/python3
"""A class representing a square.
    Private attribute:__size(int)
"""


class Square:
    def __int__(self, size=0):
        self.__size = size
        """initalizes a new square"""

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """initalizes square area"""
            return self.__size ** 2
