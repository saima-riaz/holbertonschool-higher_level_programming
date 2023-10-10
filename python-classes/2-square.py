#!/usr/bin/python3
"""A class representing a square.
    Private attribute:__size(int)
"""


class Square:
    def __int__(self, size=0):
        """initalizes a new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            size.__size = size
