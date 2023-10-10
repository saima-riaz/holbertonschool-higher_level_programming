#!/usr/bin/python3
"""A class representing a square.
    Private attribute:__size(int)
"""


class Square:
""" define square"""
    def __int__(self, size=0):
        self.__size = size
        """initalizes a 0 square"""

        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
