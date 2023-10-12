#!/usr/bin/python3
def add_integer(a, b=98):
    if (not isinstance(a, int) and not isinstance(a, float)) or \
       (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
 
    if isinstance(a, float):
        a = int(a)
        """If 'b' is a float, cast it to an integer"""
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
