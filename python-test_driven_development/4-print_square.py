#!/usr/bin/python3
""" Print a square made of '#' characters with the specified size"""


def print_square(size):

    if not isinstance(size, int):
        """Raises:
    TypeError: If 'size' is not an integer
    ValueError: If 'size' is less than 0"""

        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError(" size must be >= 0")
    for _ in range(size):
        print("#" * size)
