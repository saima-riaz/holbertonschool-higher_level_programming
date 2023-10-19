#!/usr/bin/python3
"""Rectangle heritage"""

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


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """define area"""
        return self.__width * self.__height

    def __str__(self):
        """define str"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    

class Square(Rectangle):
    """define class square(Rectangle)"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        super().__size = size

    def area(self):
        """ define area"""
        return self.__size ** 2
